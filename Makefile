JTD?=./jtd-codegen
JQ?=jq

.PHONY: python java

format:
	$(JQ) . reshare.jtd.json > .reshare.tmp && mv .reshare.tmp reshare.jtd.json

python:
	$(JTD) reshare.jtd.json --python-out python/src/reshare

java:
	$(JTD) reshare.jtd.json --java-jackson-out java/lib/src/main/java/org/reshare/ --java-jackson-package org.reshare
