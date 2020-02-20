.PHONY: start
start:
	docker-compose -f local.yml up

.PHONY: rebuild-all
rebuild-all:
	docker-compose -f local.yml down -v --rmi all
	docker-compose -f local.yml up
