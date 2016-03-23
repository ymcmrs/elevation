
DATASOURCE_URL := {datasource_url}
PRODUCT := {product}
TILE_EXT := {tile_ext}
ZIP_EXT := {zip_ext}

ENSURE_TILE_PATHS := $(foreach n,$(ENSURE_TILES),cache/$n)


all: $(PRODUCT).vrt

$(PRODUCT).vrt: $(shell ls cache/*.tif 2>/dev/null)
	gdalbuildvrt -q -overwrite $@ cache/*.tif

spool/%$(ZIP_EXT):
	curl -s -f -o $@ $(DATASOURCE_URL)/$*$(ZIP_EXT)

spool/%$(TILE_EXT): spool/%$(ZIP_EXT)
	unzip -q -d spool $< $*$(TILE_EXT)

cache/%.tif: spool/%$(TILE_EXT)
	gdal_translate -q -co TILED=YES -co COMPRESS=DEFLATE -co ZLEVEL=9 -co PREDICTOR=2 $< $@

download: $(ENSURE_TILE_PATHS)

clip: $(PRODUCT).vrt
	gdal_translate -q -co TILED=YES -co COMPRESS=DEFLATE -co ZLEVEL=9 -co PREDICTOR=2 -projwin $(PROJWIN) $(PRODUCT).vrt $(OUTPUT)

clean:
	$(RM) spool/*

distclean: clean
	$(RM) cache/* $(PRODUCT).vrt Makefile

.DELETE_ON_ERROR:
.PHONY: all download clip clean distclean

#
# override most of make default behaviour
#
# disable make builtin rules
MAKEFLAGS += --no-builtin-rules
# disable suffix rules
.SUFFIXES:
