(defproject YelpReviews "0.0.1-SNAPSHOT"
  :resource-paths ["_resources"]
  :repositories {"HDP Releases" "http://repo.hortonworks.com/content/repositories/releases"}
  :target-path "_build"
  :min-lein-version "2.0.0"
  :jvm-opts ["-client"]
  :dependencies  [[org.apache.storm/storm-core "0.10.0.2.4.2.0-258"]
                  [org.apache.storm/flux-core "0.10.0.2.4.2.0-258"]]
  :jar-exclusions     [#"log4j\.properties" #"org\.apache\.storm\.(?!flux)" #"trident" #"META-INF" #"meta-inf" #"\.yaml"]
  :uberjar-exclusions [#"log4j\.properties" #"org\.apache\.storm\.(?!flux)" #"trident" #"META-INF" #"meta-inf" #"\.yaml"]
  )
