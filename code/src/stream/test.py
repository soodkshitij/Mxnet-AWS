# import tweepy
# 
# consumer_secret =  "k0lTtj6DTsPfUWtkXynpQalFkF79xyovixmS1W6hMMN0VGJtgW"
# consumer_key = "XunErNB3P5XXRCx06KvzpgXkg"
# access_token = "1121188546318962690-R2cFYRzVMneHAPqczhO66yms9wrsG1"
# access_token_secret = "v98uvfWzP6Yk4kPgYIFNLzGtYxUeqLUJdjPyTHuvsd801"
# 
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# 
# api = tweepy.API(auth)
# 
# api.update_status('@SoodKshitij http://13.0.1.1/test', 1126433016924889088)

import pymongo
 
con = None
 
def get_mongo_connection(host='localhost', port=27017):
    global con
    if con is None:
        print "Establishing connection %s host and port %d" %(host,port)
        try:
            con = pymongo.MongoClient(host, port)
        except Exception, e:
            print e
            return None
    return con
 
x = "B00JU1O1XC.jpg","B00G3G14T6.jpg","B00F24DOBG.jpg","B00GNB7SDC.jpg","B00HV8QNOG.jpg","B00JJBA8H6.jpg","B00HSH4SFQ.jpg","B00FLS2CH0.jpg","B00ES27N7E.jpg","B00DK47NDK.jpg","B00ID8JO0I.jpg","B00FJ8BCNC.jpg","B00GW4JMIE.jpg","B00I0WTR9A.jpg","B00EAZMWU2.jpg","B00DZJLNOA.jpg","B00K4P3EZE.jpg","B00FJIXCNA.jpg","B00DSFJDQQ.jpg","B00IT5GPZ2.jpg","B00H7ND0W8.jpg","B00H7ND1XG.jpg","B00ICBRYOY.jpg","B00F117F5Q.jpg","B00GU2YHQK.jpg","B00HJ05DC4.jpg","B00DIDZ682.jpg","B00EMLLXV8.jpg","B00DBQ51ZY.jpg","B00EX7FCJ0.jpg","B00DHJPMRM.jpg","B00GDX6KE8.jpg","B00EUOABQU.jpg","B00EX7EFKM.jpg","B00DKANFQI.jpg","B00EBBH4XK.jpg","B00DNHL74A.jpg","B00GVHK5KQ.jpg","B00HQW58AM.jpg","B00ELPXIU4.jpg","B00GA1X1E0.jpg","B00DME4EL2.jpg","B00E8M6DC0.jpg","B00FZHE18U.jpg","B00FN2LLKS.jpg","B00GDDMU06.jpg","B00EO8IBL4.jpg","B00DU65EPC.jpg","B00EF8QFYS.jpg","B00E0UD71U.jpg","B00GRNQ1I4.jpg","B00F8L1MM6.jpg","B00F8L2HQQ.jpg","B00JTUD5OU.jpg","B00DUHENJY.jpg","B00F3P63FS.jpg","B00FRFFQJS.jpg","B00DOQF6GU.jpg","B00DOQF68I.jpg","B00DOQF4US.jpg","B00E1DP7H8.jpg","B00E1DPA3O.jpg","B00E1DPA1Q.jpg","B00FF1PCGQ.jpg","B00F52HHAY.jpg","B00F52HH9U.jpg","B00DG6SMR8.jpg","B00DG6SMMS.jpg","B00DG6SOVW.jpg","B00E4UIE4Q.jpg","B00J9H7FCQ.jpg","B00GV8AN9I.jpg","B00GV8ANA2.jpg","B00EONG7RY.jpg","B00DWXJWRO.jpg","B00JBLY34S.jpg","B00GEXUYR6.jpg","B00ICO4X0E.jpg","B00F4N177S.jpg","B00EUFQE4M.jpg","B00H8Z4BYQ.jpg","B00E4FQNLW.jpg","B00GR91FLQ.jpg","B00H8QASGK.jpg","B00HV5A8TU.jpg","B00GFW2LNG.jpg","B00F6E8CIC.jpg","B00FRTWA5C.jpg","B00EO3WHB4.jpg","B00FTXH2PY.jpg","B00GEXXMZM.jpg","B00GEXXL62.jpg","B00EHATZRS.jpg","B00J6CTJ8W.jpg","B00J6CT162.jpg","B00HNGO9YM.jpg","B00HS0P6OK.jpg","B00E64IA8U.jpg","B00IA9LZC0.jpg","B00HGKOIKK.jpg","B00GVA2KCY.jpg","B00ESKPVUC.jpg","B00EUJXJBO.jpg","B00DY4PD7Y.jpg","B00ESHE49Y.jpg","B00J7VJ3Y2.jpg","B00GJ40FKQ.jpg","B00FGDTLBA.jpg","B00H1AY0SA.jpg","B00GQPQB8S.jpg","B00I0HWVTI.jpg","B00IMZOLMS.jpg","B00F93D6UE.jpg","B00IK52R30.jpg","B00IK52W9Y.jpg","B00IFK9PD0.jpg","B00H20FUPQ.jpg","B00LN5PCXG.jpg","B00F0GU9FK.jpg","B00DE4P2FW.jpg","B00DQWA3DI.jpg","B00GYAK8YI.jpg","B00JBE6MV2.jpg","B00E835BEK.jpg","B00DIHING0.jpg","B00FVHCO9W.jpg","B00GD91XB2.jpg","B00E7LJWES.jpg","B00GSXWKR4.jpg","B00K0KPYM4.jpg","B00GC93XYS.jpg","B00DJ3ZZ4G.jpg","B00FJ1HFGC.jpg","B00H0PWF06.jpg","B00JGPFUK0.jpg","B00GOEJHX2.jpg","B00GOEOXHM.jpg","B00EQFIBTW.jpg","B00E1L7836.jpg","B00E1L78N6.jpg","B00EB200QW.jpg","B00I45GT3A.jpg","B00EB2003U.jpg","B00FJISZAA.jpg","B00F0UFUHI.jpg","B00EV21PN4.jpg","B00I9L4BYS.jpg","B00F6PRSMW.jpg","B00GM2K474.jpg","B00E9FYC06.jpg","B00HRXZ3QY.jpg","B00HVH8YJO.jpg","B00EDHVJ56.jpg","B00EDHVIXY.jpg","B00EDHVJBU.jpg","B00EJC0S66.jpg","B00HYPC6JC.jpg","B00ENFALFW.jpg","B00JJIX8GW.jpg","B00EECQY3C.jpg","B00JJIX8FS.jpg","B00F9SQFHK.jpg","B00K01YNCU.jpg","B00EFK8W92.jpg","B00EDSM5I0.jpg","B00H03NZB6.jpg","B00H917F4W.jpg","B00FAPA55A.jpg","B00DKEX5AU.jpg","B00HVJPBBQ.jpg","B00F95Y8RW.jpg","B00EHD7U4U.jpg","B00IL7FM3Y.jpg","B00E97SAOI.jpg","B00DZGHIJW.jpg","B00DM1GJIG.jpg","B00IOHKIKS.jpg","B00ES8KY8S.jpg","B00ICD65CO.jpg","B00IJGVZQA.jpg","B00G4BRATS.jpg","B00J9CE5HO.jpg","B00FEOLDYY.jpg","B00E0HOYD8.jpg","B00G75ZCB4.jpg","B00DEWX7UQ.jpg","B00GNWJP6E.jpg","B00G0MOI6E.jpg","B00EV6P3B0.jpg","B00KHYWR2I.jpg","B00J8UF8PA.jpg","B00GMP5Q60.jpg","B00HBKSMBG.jpg","B00IRMHGQ4.jpg","B00DM1GHO2.jpg","B00DQ2K7E8.jpg","B00DOQR82U.jpg","B00IV2RLUQ.jpg","B00DF1536C.jpg","B00DXAS00Q.jpg","B00F62A2PK.jpg","B00F62A3UE.jpg","B00F62A3IG.jpg","B00E0FRU0O.jpg","B00IULVXIO.jpg","B00IULVVSQ.jpg","B00DEEC3UO.jpg","B00DEEC3VI.jpg","B00E0FS19S.jpg","B00IOA6U0M.jpg","B00FSBS59E.jpg","B00EZ7ZSU6.jpg","B00HXC8YLU.jpg","B00HYPXIIA.jpg","B00HYPXII0.jpg","B00IDHF78M.jpg","B00FP03GLA.jpg","B00ER5DRWW.jpg","B00GB87PW6.jpg","B00GB87OA4.jpg","B00JJ5FIYA.jpg","B00FCXOM9A.jpg","B00EZPTORQ.jpg","B00EZPTO76.jpg","B00EZPTNTA.jpg","B00FXAAAMK.jpg","B00FXAABZG.jpg","B00EFXC9ES.jpg","B00EFXC650.jpg","B00EFXC8BM.jpg","B00EFXCB8W.jpg","B00EFXCADS.jpg","B00EFXC4UW.jpg","B00EFXC9DY.jpg","B00EFXC65U.jpg","B00EFXC78G.jpg","B00EFXBWP0.jpg","B00EFXC99S.jpg","B00EFXC7GI.jpg","B00EVOD3MI.jpg","B00EVODA3K.jpg","B00DYRBHXA.jpg","B00DYRBJC4.jpg","B00DYRBG9A.jpg","B00DB20M70.jpg","B00D9JSSS0.jpg","B00F5XV24A.jpg","B00F5XWBY0.jpg","B00F61A5SK.jpg","B00DVEHM76.jpg","B00E1FHXBE.jpg","B00E1FI5FC.jpg","B00GXW435W.jpg","B00I2ICEYM.jpg","B00F59LT74.jpg","B00FSK7JXI.jpg","B00E2SFYES.jpg","B00E1FI7HS.jpg","B00DQKJIP4.jpg","B00HG9MQO6.jpg","B00J0V3AZW.jpg","B00GA9WNTQ.jpg","B00F63LM8A.jpg","B00GAPU4KK.jpg","B00I47ARL8.jpg","B00HZMPHI6.jpg","B00GBDE55G.jpg","B00GXW465Y.jpg","B00EEBDBR0.jpg","B00F63PSKI.jpg","B00F8K22V2.jpg","B00GXW3XTY.jpg","B00GIVASDE.jpg","B00GIV0RGM.jpg","B00GIV743G.jpg","B00K31DRMY.jpg","B00GYZO33K.jpg","B00GYZO4CK.jpg","B00KH906L2.jpg","B00I8R0OFI.jpg","B00GYZOB1O.jpg","B00JWKAZNG.jpg","B00GYZNJ4E.jpg","B00GYZNUVG.jpg","B00GYZH71A.jpg","B00E3I7FYE.jpg","B00E3I74Y0.jpg","B00E3I72W4.jpg","B00GYZNOB2.jpg","B00GYZNNCW.jpg","B00H8Z2G7U.jpg","B00H8Z52XU.jpg","B00ICUQ4IW.jpg","B00ICUQ3JW.jpg","B00F40QQZY.jpg","B00FLDIBWU.jpg","B00GYZQGF8.jpg","B00IKI16LG.jpg","B00HS7PYHC.jpg","B00HQC9FIS.jpg","B00EUMFC2A.jpg","B00H3ZO8MG.jpg","B00GLOPQD0.jpg","B00DT3FBVS.jpg","B00FA4TWKA.jpg","B00GEWRTR0.jpg","B00EEBE124.jpg","B00K92JHX0.jpg","B00I1M0FZ4.jpg","B00I9ZEUT0.jpg","B00GTEX6UC.jpg","B00DCCPD5K.jpg","B00DJR11VI.jpg","B00FECEP6O.jpg","B00ILOEP3A.jpg","B00I1L2350.jpg","B00HZAFHWE.jpg","B00EKLQ95U.jpg","B00EYQVRRG.jpg","B00GTEX65M.jpg","B00I149O6I.jpg","B00GU5TESI.jpg","B00FRWI648.jpg","B00FZQCZZW.jpg","B00I1LM5SK.jpg","B00D9VQRJA.jpg","B00D9VQRIG.jpg","B00DEP3AVY.jpg","B00EW67XV2.jpg","B00FJXSLAE.jpg","B00EA2PD60.jpg","B00EMI7MIY.jpg","B00EGP1JSC.jpg","B00HEU44DS.jpg","B00DZ42F10.jpg","B00EQ2K4JU.jpg","B00GMGZZ0G.jpg","B00EHQJPPO.jpg","B00EHQJR0C.jpg","B00FEX6CFK.jpg","B00ECUTFFU.jpg","B00ED47EIK.jpg","B00JBAVNZQ.jpg","B00FABT5VO.jpg","B00L5OHCPQ.jpg","B00FS6MLZ8.jpg","B00GDQFN70.jpg","B00ELOJDHM.jpg","B00GGLZZW0.jpg","B00FSZKUV6.jpg","B00G1YKHES.jpg","B00HIYA4F2.jpg","B00IJN0PW8.jpg","B00FR73KGW.jpg","B00HPR7K8Q.jpg","B00FDTJF04.jpg","B00HBUWOME.jpg","B00DPPOI5U.jpg","B00IUOU6MA.jpg","B00FB4PMWG.jpg","B00FB45YI8.jpg","B00DTWN9U4.jpg","B00F9VPH5S.jpg","B00HQZGZ38.jpg","B00EEY89X8.jpg","B00GPUFAB8.jpg","B00FIS1LU2.jpg","B00HRO32J8.jpg","B00L1FUOIG.jpg","B00JXLGEE8.jpg","B00HXE4CZ0.jpg","B00F9VPIXO.jpg","B00HNWLYSK.jpg","B00DNR3HP2.jpg","B00HO5JF7S.jpg","B00GD2EBCC.jpg","B00JG1NIQC.jpg","B00FQ2BS5S.jpg","B00JG1MZLQ.jpg","B00E1QMBX8.jpg","B00FF59JLG.jpg","B00F06CKOS.jpg","B00HFLJGIY.jpg","B00HS73V5E.jpg","B00E6DMKXM.jpg","B00EIQVZX8.jpg","B00H4FJC2G.jpg","B00JBK04BK.jpg","B00JBK02Z8.jpg","B00JBK02EY.jpg","B00JDKJQV2.jpg","B00G9FFFTG.jpg","B00FRAWGAU.jpg","B00GKBE1KS.jpg","B00KOZ3S4G.jpg","B00I3OCC5G.jpg","B00F0TMMKM.jpg","B00FGIBTCE.jpg","B00FKZLI8S.jpg","B00DMAM82S.jpg","B00HTMDEH8.jpg","B00ENVX6SK.jpg","B00GKWPZMU.jpg","B00ITK3GZE.jpg","B00F70H40M.jpg","B00HPLOE18.jpg","B00HXAV7KM.jpg","B00GJ2E8F6.jpg","B00GWKKX0O.jpg","B00FDHLKVS.jpg","B00IA3YLKY.jpg","B00DT77GHG.jpg","B00FWVGY48.jpg","B00EXFSEJ2.jpg","B00GD1RVQG.jpg","B00GWTU4R2.jpg","B00EWJNJHG.jpg","B00DZF2JLA.jpg","B00HA3DJMG.jpg","B00H5E0KO0.jpg","B00F4714IG.jpg","B00I51I1RK.jpg","B00I51I2E2.jpg","B00FJVE1NC.jpg","B00IIA9NDO.jpg","B00K5ZRUZ8.jpg","B00K5ZRUEY.jpg","B00HYOGTR8.jpg","B00GSDVKZW.jpg","B00GSDVKX4.jpg","B00K5ZRUT4.jpg","B00K5ZRTFO.jpg","B00KJ1K59Q.jpg","B00K5ZRVHU.jpg","B00K5ZRTCM.jpg","B00HLNXTPM.jpg","B00K5ZRSP0.jpg","B00HRAXUH6.jpg","B00ESM9ONA.jpg","B00EU7NVKU.jpg","B00DXZXC7W.jpg","B00EVB5478.jpg","B00DFI8ED4.jpg","B00HYAKJO6.jpg","B00EA996PC.jpg","B00IAEHFH4.jpg","B00IRRIJQA.jpg","B00DS58QI2.jpg","B00GJXVZ24.jpg","B00GT33JFA.jpg","B00DW2GIGI.jpg","B00I84KMJE.jpg","B00EUGAEMO.jpg","B00DW2GB6U.jpg","B00DW2GB4W.jpg","B00DW2GB38.jpg","B00E1O4JE4.jpg","B00DUIOFJQ.jpg","B00DT1XUGI.jpg","B00E0I71OG.jpg","B00E0I71V4.jpg","B00DHG0NNI.jpg","B00DHFFRWG.jpg","B00DHG2D54.jpg","B00FQMAQLA.jpg","B00H2T13AS.jpg","B00F2KC8EE.jpg","B00FY4NWZ2.jpg","B00FHT6NS2.jpg","B00DHFV91Y.jpg","B00EB94CKK.jpg","B00G6T5R02.jpg","B00G6T5TZ0.jpg","B00H3U26LG.jpg","B00H3U2CIS.jpg","B00FIECA42.jpg","B00FIEC9YI.jpg","B00F5UFSNY.jpg","B00F5UG4TG.jpg","B00FKVYEWO.jpg","B00F1CDM2U.jpg","B00F1CDNU6.jpg","B00EHJ2I46.jpg","B00IP1HKG8.jpg","B00DV901EW.jpg","B00EIRRD8I.jpg","B00EIRRCR0.jpg","B00K7K9VLW.jpg","B00J8UZEX6.jpg","B00J8UZT54.jpg","B00J8UZJPE.jpg","B00ID1W8GM.jpg","B00FSDC5YS.jpg","B00HSRO47I.jpg","B00DH85SD6.jpg","B00DH85QJC.jpg","B00G0KSPVU.jpg","B00GEJMTMI.jpg","B00GSPM8YC.jpg","B00IU2VB6W.jpg","B00IP3TN48.jpg","B00FI5XHSE.jpg","B00HCDB3GI.jpg","B00E86CUYQ.jpg","B00EKS33FC.jpg","B00JAXUTGI.jpg","B00HV053J0.jpg","B00J4O74KC.jpg","B00HAZOSWY.jpg","B00IYIOHF4.jpg","B00JXO51P8.jpg","B00FXWNNW2.jpg","B00FORG69I.jpg","B00EKVXDWM.jpg","B00HC3YW8E.jpg","B00DWG3DOY.jpg","B00H8XJ5EO.jpg","B00IJSB76Q.jpg","B00F2OJS6Q.jpg","B00EWHJWLU.jpg","B00ESUIU7I.jpg","B00DVMFVKS.jpg","B00F1JV9X2.jpg","B00G0Y90X8.jpg","B00DWGT71M.jpg","B00HJ2OYPY.jpg","B00FX411P6.jpg","B00HNICPLO.jpg","B00GCRHSB4.jpg","B00HY86FXW.jpg","B00HA41WRE.jpg","B00HY7IPJA.jpg","B00EEEE7IO.jpg","B00FT2TAGY.jpg","B00FFDY12A.jpg","B00GHTLWK0.jpg","B00JC5NFW4.jpg","B00ETAHD16.jpg","B00EXUI3XO.jpg","B00DT1ONZ0.jpg","B00FJC672E.jpg","B00HJ18I16.jpg","B00HJKK38I.jpg","B00HQP8Z18.jpg","B00G06CHFE.jpg","B00DO5V3W2.jpg","B00FCKHROK.jpg","B00HNNI2Y8.jpg","B00EK3J06I.jpg","B00EXVYCJW.jpg","B00GB9K11W.jpg","B00EO5WVKY.jpg","B00F6J7H0G.jpg","B00H57ZUE2.jpg","B00GOTBN9I.jpg","B00DJWJFW0.jpg","B00DD0VEJU.jpg","B00HTLXHCG.jpg","B00DY3U8MU.jpg","B00I4CDJ22.jpg","B00DQYPAOS.jpg","B00GP2833I.jpg","B00E6XNQGM.jpg","B00G3D3DVQ.jpg","B00I4QTJRC.jpg","B00G3D3BM2.jpg","B00F9HVPFS.jpg","B00I4QTJMM.jpg","B00FPKCY6I.jpg","B00F9P2YSC.jpg","B00ELP2UVW.jpg","B00H9LLFJ8.jpg","B00EO5WTC4.jpg","B00DP5F6OC.jpg","B00DD0CU98.jpg"
 
c = 1
for i in x:
    a = i.split(".")[0]
    r = list(get_mongo_connection().catalog.products.find({'asin':a}))
     
    if not r:
        c+=1
        print a
print c
     