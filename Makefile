# Makefile for caffeine

release:
	bzr diff && \
	rm -rf ./dist && \
	python3 setup.py sdist bdist_wheel && \
	twine upload dist/* && \
	bzr tag $$(python3 setup.py --version|tail -1) && \
	bzr push
