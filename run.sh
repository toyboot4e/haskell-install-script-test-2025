cp "$1" src/source &&
python3 src/parse.py &&
docker build --platform linux/amd64 -t atcoder -f src/Dockerfile . && 
docker run --rm -it atcoder
