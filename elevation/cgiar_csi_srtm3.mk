
BASE_URL := http://srtm.csi.cgiar.org
VERSION := {version}
FOLDER_PATH := SRT-ZIP/SRTM_$(VERSION)/SRTM_Data_GeoTiff
DATASOURCE := {datasource}

ENSURE_TILE_PATHS := $(foreach n,$(ENSURE_TILES),cache/$n)


all: $(DATASOURCE).vrt

$(DATASOURCE).vrt: $(shell ls cache/*.tif 2>/dev/null) $(ENSURE_TILE_PATHS)
	gdalbuildvrt -q -overwrite $@ cache/*.tif

spool/%.zip:
	curl -s -o $@ $(BASE_URL)/$(FOLDER_PATH)/$*.zip

spool/%.tif: spool/%.zip
	unzip -q -d spool $< $*.tif

cache/%.tif: spool/%.tif
	gdal_translate -q -co TILED=YES -co COMPRESS=DEFLATE -co ZLEVEL=9 -co PREDICTOR=2 $< $@

clip: $(DATASOURCE).vrt
	gdal_translate -q -co TILED=YES -co COMPRESS=DEFLATE -co ZLEVEL=9 -co PREDICTOR=2 -projwin $(PROJWIN) $(DATASOURCE).vrt $(OUT_PATH)

clean:
	$(RM) spool/*

distclean: clean
	$(RM) cache/* $(DATASOURCE).vrt Makefile

.DELETE_ON_ERROR:
.PRECIOUS: spool/%.zip
.PHONY: all clean distclean clip

#
# override most of make default behaviour
#
# disable make builtin rules
MAKEFLAGS += --no-builtin-rules
# disable suffix rules
.SUFFIXES:
