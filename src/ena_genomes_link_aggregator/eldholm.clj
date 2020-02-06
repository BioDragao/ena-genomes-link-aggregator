(ns ena-genomes-link-aggregator.eldholm
  (:use etaoin.api)
  (:require [etaoin.keys :as keys]
            [clojure.edn :as edn]))

;;;;;;;;;

(def genomes
  [
   "BRZ-260",
   "BRZ-116",
   "BRZ-265",
   "BRZ-266",
   "BRZ-267",
   "BRZ-268",
   "BRZ-269",
   "BRZ-117",
   "BRZ-270",
   "BRZ-271",
   "BRZ-272",
   "BRZ-273",
   "BRZ-274",
   "BRZ-275",
   "BRZ-276",
   "BRZ-277",
   "BRZ-113",
   "BRZ-114",
   "BRZ-115",
   "BRZ-294",
   "BRZ-119",
   "BRZ-283",
   "BRZ-120",
   "BRZ-121",
   "BRZ-122",
   "BRZ-123",
   "BRZ-124",
   "BRZ-126",
   "BRZ-127",
   "BRZ-291",
   "BRZ-292",
   "BRZ-293",
   "BRZ-280",
   "BRZ-295",
   "BRZ-297",
   "BRZ-259",
   "BRZ-285",
   "BRZ-261",
   "BRZ-263",
   "BRZ-264",
   "BRZ-303",
   "BRZ-278",
   "BRZ-279",
   "BRZ-288",
   "BRZ-298",
   "BRZ-281",
   "BRZ-282",
   "BRZ-289",
   "BRZ-286",
   "BRZ-287",
   "BRZ-300",
   "BRZ-302",
   "BRZ-290",
   "BRZ-301",
   ])

(def driver (firefox {:path-driver  "/usr/local/bin/geckodriver"
                      :path-browser "/Applications/Firefox Developer Edition.app/Contents/MacOS/firefox"}))

;;;;;;;;;


(go driver "https://www.ebi.ac.uk/ena")

(defn extract-r-file-links-for-a-genome [genome-id]
  (clear driver {:id "local-searchbox"})
  (fill driver {:id "local-searchbox"} genome-id)
  (click-el driver
            (query driver {:fn/has-class "submit"}))

  (wait driver 40)

  (println genome-id)
  (println
    (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(1)"} :href))
  (println
    (get-element-attr driver {:css "td.resultReportsCell:nth-child(30) > div:nth-child(1) > a:nth-child(3)"} :href)))



(map extract-r-file-links-for-a-genome genomes)



