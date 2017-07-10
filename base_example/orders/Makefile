TAG ?= dev
# docker

run-wheel-builder:
	docker run --rm \
		-v "$$(pwd)":/application -v "$$(pwd)"/wheelhouse:/wheelhouse \
		simplebank-builder;

build-image:
	docker build -t microservicesinaction/simplebank-orders:$(TAG) -f docker.run .;

push-image:
	docker push microservicesinaction/simplebank-orders:$(TAG)
