build-api-image:
	docker build -f Dockerfile -t fast_api:v1 .

run-api-server:
	docker-compose -f docker-compose.yaml up -d

down-api-server:
	docker-compose -f docker-compose.yaml down

run-api-server-local:
	uvicorn app.main:app