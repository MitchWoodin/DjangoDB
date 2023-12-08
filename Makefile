coverage:
	pytest --cov=api --migrations -n 2 --dist loadfile


fcov:
	@echo "Running fast coverage check"
	@pytest --cov=api -n 4 --dist loadfile -q
