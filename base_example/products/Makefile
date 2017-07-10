TAG ?= dev
# docker

run-wheel-builder:
	docker run --rm \
		-v "$$(pwd)":/application -v "$$(pwd)"/wheelhouse:/wheelhouse \
		simplebank-builder;

build-image:
	docker build -t microservicesinaction/simplebank-products:$(TAG) -f docker.run .;

push-image:
	docker push microservicesinaction/simplebank-products:$(TAG)
