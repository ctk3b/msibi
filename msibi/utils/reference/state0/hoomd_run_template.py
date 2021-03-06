all = group.all()
nvt_int = integrate.bdnvt(group=all, T=T_final)
integrate.mode_standard(dt=0.001)


run(5000)
output_dcd = dump.dcd(filename="query.dcd", period=1e3, overwrite=True)
run(50000)

output_xml = dump.xml()
output_xml.set_params(all=True)
output_xml.write(filename="final.xml")
