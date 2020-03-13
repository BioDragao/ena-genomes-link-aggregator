(ns ena-genomes-link-aggregator.richard_genomes
  (:use etaoin.api)
  (:require [etaoin.keys :as keys]
            [clojure.edn :as edn]))


;;;;;;;;;
(def richard-genomes-edn
  (edn/read-string
    (slurp "./src/ena_genomes_link_aggregator/richard.edn")))


(def driver (firefox {:path-driver  "/usr/local/bin/geckodriver"
                      :path-browser "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"}))

;;;;;;;;;

(defn extract-r-file-links-for-a-genome [genome-id]
  (go driver (str "https://www.ebi.ac.uk/ena/data/view/" genome-id))

  (wait driver 10)

  (println genome-id)
  (println
    (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(1)"} :href))
  (println
    (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(3)"} :href)))


(map extract-r-file-links-for-a-genome richard-genomes-edn)





