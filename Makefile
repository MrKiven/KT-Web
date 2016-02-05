run:
	python run.py

unittest:
	mkdir -p .build
	py.test tests -rfExswX --duration=10 --junitxml=.build/unittest.xml --cov kt_web --cov-report xml -n 4
