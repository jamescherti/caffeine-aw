# Makefile for caffeine

.PHONY:	dist

dist:
	rm -rf ./dist && \
	python3 setup.py sdist bdist_wheel

release: dist
	bzr diff && \
	twine upload dist/* && \
	bzr tag $$(python3 setup.py --version|tail -1) && \
	bzr push
