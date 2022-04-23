FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

# RDEPENDS_${PN}-inventory_${MACHINE} += "webui-vue"
RDEPENDS_${PN}-inventory_${MACHINE} += "phosphor-webui"

PACKAGES:remove:viscore-nohost = "\
        ${PN}-console \
        "
