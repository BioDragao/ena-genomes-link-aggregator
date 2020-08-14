(ns ena-genomes-link-aggregator.xdr-and-mdr-latin-america
  (:use etaoin.api)
  (:require [clojure.edn :as edn]
            [cognitect.transit :as t]
            [cheshire.core :refer :all]
            [taoensso.timbre :as timbre]
            [com.wsscode.edn-json :refer :all]
            [taoensso.timbre.appenders.core :as appenders]
            [clj-http.client :as client]
            [clojure.java.io :as io]))

(def mdr-and-xdr-latin-america-edn
  (edn/read-string
    (slurp "./src/ena_genomes_link_aggregator/xdr_and_mdr_latin_america.edn")))


(defn get-genome-url [run-accession]
  (str
    "https://www.ebi.ac.uk/ena/portal/api/filereport?accession="
    run-accession
    "&result=read_run&fields=study_accession,sample_accession,experiment_accession,run_accession,tax_id,scientific_name,fastq_ftp,submitted_ftp,sra_ftp&format=json&download=true"))


(defn fetch-edn
  "
  Makes an HTTP request and fetches the binary object
  "
  [url]
  (let [req (client/get url {:accept :json})]
    (if (= (:status req) 200)
      (first (parse-string (:body req) true)))))


(comment
  (fetch-edn (get-genome-url "ERR751350"))

  '())


(def all-genomes-edn
  (map (fn [genome-id]
         (fetch-edn (get-genome-url genome-id)))
       mdr-and-xdr-latin-america-edn))


(comment

  (take 5 all-genomes-edn)

  (count all-genomes-edn)


  (with-open [w (clojure.java.io/writer "./all_genomes.edn.bak")]
    (binding [*print-length* false
              *out* w]
      (pr all-genomes-edn)))



  '())

(defn save-json
  "
  Downloads and stores the json on disk
  "
  [{:keys [url folder file-name]}]
  (some-> (fetch-edn url)
          (io/copy (io/file folder (str file-name ".json")))))


(comment
  (save-json {:folder    "/Users/eklavya/projects/scientific/"
              :url       "https://www.ebi.ac.uk/ena/portal/api/filereport?accession=ERR751350&result=read_run&fields=study_accession,sample_accession,experiment_accession,run_accession,tax_id,scientific_name,fastq_ftp,submitted_ftp,sra_ftp&format=json&download=true"
              :file-name "test"})

  '())

