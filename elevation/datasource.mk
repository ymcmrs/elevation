
DATASOURCE_URL := {datasource_url}
PRODUCT := {product}
TILE_EXT := {tile_ext}
ZIP_EXT := {zip_ext}

ENSURE_TILE_PATHS := $(foreach n,$(ENSURE_TILES),cache/$n)
STDERR_SWITCH := 2>/dev/null

all: $(PRODUCT).vrt

$(PRODUCT).vrt: $(shell find cache -size +0 -name "*.tif" 2>/dev/null)
	gdalbuildvrt -q -overwrite $@ $^

spool/%$(ZIP_EXT):
	curl -s -o $@.temp $(DATASOURCE_URL)/$*$(ZIP_EXT) && mv $@.temp $@

spool/%$(TILE_EXT): spool/%$(ZIP_EXT)
	unzip -qq -d spool $< $*$(TILE_EXT) $(STDERR_SWITCH) || touch $@

cache/%.tif: spool/%$(TILE_EXT)
	gdal_translate -q -co TILED=YES -co COMPRESS=DEFLATE -co ZLEVEL=9 -co PREDICTOR=2 $< $@ $(STDERR_SWITCH) || touch $@

download: $(ENSURE_TILE_PATHS)

clip: $(PRODUCT).vrt
	gdal_translate -q -co TILED=YES -co COMPRESS=DEFLATE -co ZLEVEL=9 -co PREDICTOR=2 -projwin $(PROJWIN) $(PRODUCT).vrt $(OUTPUT)

info:
	@echo 'Product folder: $(shell pwd)'
	@echo 'Tiles count: $(shell ls cache/*.tif | wc -l)'
	@echo 'Cache size: $(shell du -sh .)'

clean:
	find cache -size 0 -name "*.tif" -delete
	$(RM) spool/*

distclean: clean
	$(RM) cache/* $(PRODUCT).vrt Makefile

.DELETE_ON_ERROR:
.PHONY: all info download clip clean distclean

#
# override most of make default behaviour
#
# disable make builtin rules
MAKEFLAGS += --no-builtin-rules
# disable suffix rules
.SUFFIXES:
