FROM ubuntu AS build-stage

RUN echo "build..." > /build.txt

FROM ubuntu AS test-stage

COPY --from=build-stage /build.txt /build.txt
RUN echo "test..." >> text.txt

FROM ubuntu

COPY --from=test-stage /build.txt /build.txt

CMD cat /build.txt
