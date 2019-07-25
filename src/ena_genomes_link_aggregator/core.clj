(ns ena-genomes-link-aggregator.core
  (:use etaoin.api)
  (:require [etaoin.keys :as keys]
            [clojure.edn :as edn]))



;;;;;;;;;


(def genomes
  ["ERR502500"])

(def driver (firefox {:path-driver "/usr/local/bin/geckodriver"
                      :path-browser "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"}))


;;;;;;;;;


(println  "Now we are on the main website")

(go driver "https://www.ebi.ac.uk/ena")

                                        ;(fill driver {:id "local-searchbox"} "ERR036201")
                                        ; SRR5065386

(defn extract-r-file-links-for-a-genome [genome-id]

  (clear driver {:id "local-searchbox"})

  (fill driver {:id "local-searchbox"} genome-id)

  (click-el driver
            (query driver {:fn/has-class "submit"}))

  (wait driver 5)

  (click-el driver (nth (query-all driver {:css "#enaIndexerContents > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > a:nth-child(1)"}) 0))

  (wait driver 5)

  (println genome-id)

  (println
   (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(1)"} :href))

  (println
   (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(3)"} :href))

;; TODO: Instead of try-catch, focus on the content of the field << Library layout>> - if it's << SINGLE >> then there's only one genome. Otherwise, there are two genomes
;; NOTE: CSS Selector for the field << td.resultReportsCell:nth-child(14) > div:nth-child(1) > div:nth-child(1) >>
;; (try
;;   (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(3)"} :href)
;;   (catch Exception e (str "Only one link here" )))
  )


                                        ;(extract-r-file-links-for-a-genome "SRR5065386")

                                        ;(extract-r-file-links-for-a-genome "ERR551617")


(map extract-r-file-links-for-a-genome genomes)



;; ;;;;;;;;;

;; (println "Now we are on the search result page")

;; (click-el driver (nth (query-all driver {:css "#enaIndexerContents > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > a:nth-child(1)"}) 0))

;; ;;;;;;;;;

;; (println "Now we are on the genome page")

;; ;; Link to first file
;; (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(1)"} :href)

;; ;; Link to second file
;; (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(3)"} :href)


;;;;;;;;;; SCRATCH


(def doubtful-genomes
  [;; NotEXIST :  ERR7051290
   ])




;; NOTE: To check if the genome doesn't exist


(get-element-text driver {:css ".strapline"})

(defn does-genome-exist [genome-id]

  (clear driver {:id "local-searchbox"})

  (fill driver {:id "local-searchbox"} genome-id)

  (click-el driver
            (query driver {:fn/has-class "submit"}))

  (wait driver 5)

  (if
   (= (get-element-text driver {:css ".strapline"}) "No results found for:")
    (println "NotEXIST : " genome-id)
    (println "EXIST : " genome-id)))


;; Test the function


                                        ;(does-genome-exist "ERR7051290")


(map does-genome-exist doubtful-genomes)


