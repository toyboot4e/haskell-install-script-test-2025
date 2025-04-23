cp "CheckSource.hs" src/source &&
  python3 src/parse.py &&
  docker build --platform linux/amd64 -t atcoder -f src/Dockerfile . &&
  docker run --rm -it atcoder
