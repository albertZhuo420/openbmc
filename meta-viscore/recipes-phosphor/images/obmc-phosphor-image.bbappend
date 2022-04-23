require recipes-phosphor/images/viscore-phosphor-image.inc

# OBMC_IMAGE_EXTRA_INSTALL_${MACHINE} += "webui-vue"
OBMC_IMAGE_EXTRA_INSTALL_${MACHINE} += "phosphor-webui"

# Please do not add any content directly to this file.  Instead add it to
# the corresponding .inc file.  Otherwise, builds from viscore/openbmc will
# not be able to pick up your content.
