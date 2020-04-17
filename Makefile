

ts := `/bin/date "+%Y-%m-%d_%H-%M-%S"`

default:

all: compress upload

compress:
	tar -zcf data/exports/mushsnap_dataset_$(ts).tar.gz data/data

timestamp:
	@echo Timestamp is $(ts)
	@sleep 10
	@echo Timestamp is $(ts)

