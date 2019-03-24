(ns ena-genomes-link-aggregator.core
  (:use etaoin.api)
  (:require [etaoin.keys :as keys]
            [clojure.edn :as edn]))



;;;;;;;;;

(def genomes
  [
   "ERR502500"
   "ERR751290"
   "ERR751291"
   "ERR751292"
   "ERR751293"
   "ERR751294"
   "ERR751295"
   "ERR751296"
   "ERR751297"
   "ERR751298"
   "ERR751299"
   "ERR751300"
   "ERR751301"
   "ERR751302"
   "ERR751303"
   "ERR751304"
   "ERR751305"
   "ERR751306"
   "ERR751307"
   "ERR751308"
   "ERR751309"
   "ERR751310"
   "ERR751311"
   "ERR751312"
   "ERR751313"
   "ERR751314"
   "ERR751315"
   "ERR751319"
   "ERR751320"
   "ERR751321"
   "ERR751322"
   "ERR751323"
   "ERR751324"
   "ERR751327"
   "ERR751328"
   "ERR751329"
   "ERR751330"
   "ERR751331"
   "ERR751332"
   "ERR751333"
   "ERR751334"
   "ERR751335"
   "ERR751336"
   "ERR751337"
   "ERR751338"
   "ERR751339"
   "ERR751341"
   "ERR751342"
   "ERR751343"
   "ERR751344"
   "ERR751345"
   "ERR751346"
   "ERR751348"
   "ERR751349"
   "ERR751347"
   "ERR751326"
   "ERR751325"
   "ERR751318"
   "ERR751317"
   "ERR702436"

   ])




(def driver (firefox {:path-browser "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"}))

;;;;;;;;;

(println  "Now we are on the main website")

(go driver "https://www.ebi.ac.uk/ena")

;(fill driver {:id "local-searchbox"} "ERR036201")
; SRR5065386

(defn extract-r-file-links-for-a-genome [genome-id]

  (clear driver {:id "local-searchbox"} )

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
  [
   ;; NotEXIST :  ERR7051290
   ;; NotEXIST :  ERR7051291
   ;; NotEXIST :  ERR7051292
   ;; NotEXIST :  ERR7051293
   ;; NotEXIST :  ERR7051294
   ;; NotEXIST :  ERR7051295
   ;; NotEXIST :  ERR7051296
   ;; NotEXIST :  ERR7051297
   ;; NotEXIST :  ERR7051298
   ;; NotEXIST :  ERR7051299
   ;; NotEXIST :  ERR7051300
   ;; NotEXIST :  ERR7051301
   ;; NotEXIST :  ERR7051302
   ;; NotEXIST :  ERR7051303
   ;; NotEXIST :  ERR7051304
   ;; NotEXIST :  ERR7051305
   ;; NotEXIST :  ERR7051306
   ;; NotEXIST :  ERR7051307
   ;; NotEXIST :  ERR7051308
   ;; NotEXIST :  ERR7051309
   ;; NotEXIST :  ERR7051310
   ;; NotEXIST :  ERR7051311
   ;; NotEXIST :  ERR7051312
   ;; NotEXIST :  ERR7051313
   ;; NotEXIST :  ERR7051314
   ;; NotEXIST :  ERR7051315
   ;; NotEXIST :  ERR7051319
   ;; NotEXIST :  ERR7051320
   ;; NotEXIST :  ERR7051321
   ;; NotEXIST :  ERR7051322
   ;; NotEXIST :  ERR7051323
   ;; NotEXIST :  ERR7051324
   ;; NotEXIST :  ERR7051327
   ;; NotEXIST :  ERR7051328
   ;; NotEXIST :  ERR7051329
   ;; NotEXIST :  ERR7051330
   ;; NotEXIST :  ERR7051331
   ;; NotEXIST :  ERR7051332
   ;; NotEXIST :  ERR7051333
   ;; NotEXIST :  ERR7051334
   ;; NotEXIST :  ERR7051335
   ;; NotEXIST :  ERR7051336
   ;; NotEXIST :  ERR7051337
   ;; NotEXIST :  ERR7051338
   ;; NotEXIST :  ERR7051339
   ;; NotEXIST :  ERR7051341
   ;; NotEXIST :  ERR7051342
   ;; NotEXIST :  ERR7051343
   ;; NotEXIST :  ERR7051344
   ;; NotEXIST :  ERR7051345
   ;; NotEXIST :  ERR7051346
   ;; NotEXIST :  ERR7051348
   ;; NotEXIST :  ERR7051349
   ;; NotEXIST :  ERR7051347
   ;; NotEXIST :  ERR7051326
   ;; NotEXIST :  ERR7051325
   ;; NotEXIST :  ERR7051318
   ;; NotEXIST :  ERR7051317


])




;; NOTE: To check if the genome doesn't exist
(get-element-text driver {:css ".strapline"})


(defn does-genome-exist [genome-id]

  (clear driver {:id "local-searchbox"} )

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


