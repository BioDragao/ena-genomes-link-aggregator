(ns ena-genomes-link-aggregator.genomes
  (:use etaoin.api)
  (:require [etaoin.keys :as keys]
            [clojure.edn :as edn]))




;;;;;;;;;

(def driver (firefox {:path-driver "/usr/local/bin/geckodriver"
                      :path-browser "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"}))

;;;;;;;;;

(comment
  {:number-of-files 1, :ena-url "https://www.ebi.ac.uk/ena/data/view/SRX007724"})

(def genomes-edn
  (edn/read-string
   (slurp "./src/ena_genomes_link_aggregator/genomes.edn")))


;;;;;;;;;

(defn extract-r-file-links-for-a-genome [a-genome-edn]
  (go driver (:ena-url a-genome-edn))

  (wait driver 5)

  (println
   (get-element-attr driver
                     {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(1)"}
                     :href)
   (try
     (get-element-attr driver
                       {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(3)"}
                       :href)
     (catch Exception e #_(println "Only 1 file")))

   (try
     (get-element-attr driver
                       {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(5)"}
                       :href)
     (catch Exception e #_(println "Only 2 file")))))



;;;;;;;;;
;; MAIN
;;;;;;;;;

;; (map extract-r-file-links-for-a-genome [{:ena-url "https://www.ebi.ac.uk/ena/data/view/SRR650226"
;;                                          :number-of-files 3}])




(map extract-r-file-links-for-a-genome genomes-edn)


