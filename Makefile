

ts := `/bin/date "+%Y-%m-%d_%H-%M-%S"`

default:

all: compress upload

compress:
	tar -zcf data/exports/mushsnap_dataset_$(ts).tar.gz dataset
	env DATASET_ZIP=data/exports/mushsnap_dataset_$(ts).tar.gz
	echo mushsnap_dataset_$(ts)

upload:
	python src/upload_data.py $DATASET_ZIP

timestamp:
	@echo Timestamp is $(ts)
	@sleep 10
	@echo Timestamp is $(ts)

