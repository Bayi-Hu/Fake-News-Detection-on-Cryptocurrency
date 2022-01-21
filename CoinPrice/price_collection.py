import json

pump_time_list = "1641980273,1641717008,1641600633,1641114733,1641114007,1640946739,1640672839,1640672008,1640516036,1640504749,1640412833,1640411738,1640337700,1640321377,1640320769,1639818000,1639720060,1639637572,1639634683,1639630042,1639593162,1639000815,1638987613,1638960855,1638864022,1638777604,1638744303,1638687648,1638593970,1638444613,1638246673,1638143343,1638134510,1638096829,1638090005,1638086480,1638085730,1638084392,1638054571,1638003046,1638002246,1637981374,1637871573,1637860912,1637650803,1637639690,1637574469,1637488808,1637472462,1637464091,1637386591,1637291018,1637050966,1637049608,1636873206,1636704007,1636703026,1636702586,1636699023,1636696780,1636604963,1636448171,1636400940,1636351922,1636282696,1636276909,1636275603,1636167741,1636110693,1636076778,1636004192,1636002968,1635990101,1635927954,1635892180,1635840973,1635749828,1635671189,1635670805,1635663606,1635643743,1635586236,1635581174,1635542678,1635340433,1635239186,1635232537,1635216402,1635074148,1635066007,1635058040,1635055201,1635037548,1634977881,1634976953,1634880507,1634803210,1634786672,1634785148,1634773272,1634720063,1634619822,1634464106,1634426874,1634376916,1634375642,1634372418,1634284327,1634215747,1634194806,1634106475,1634105797,1634030398,1634029092,1634009781,1634005670,1633856405,1633815076,1633771257,1633761492,1633756421,1633732063,1633681055,1633678974,1633668007,1633666253,1633638306,1633556381,1633555652,1633428952,1633417207,1633409696,1633251607,1633251088,1633167160,1633143790,1633142582,1632982042,1632809928,1632539251,1632378024,1632297604,1632291842,1632287667,1632287225,1632203406,1632042011,1632034279,1631940425,1631696405,1631690990,1631593823,1631527841,1631421638,1631347215,1631334164,1631331738,1631316248,1631266878,1631247375,1631247192,1631180900,1631167208,1631060811,1630996083,1630918411,1630897567,1630855960,1630834747,1630832438,1630810992,1630749614,1630573380,1630456684,1630320045,1630227607,1630215496,1630212873,1630063622,1630051206,1630050621,1629758304,1629737490,1629635474,1629622811,1629609059,1629532808,1629522255,1629438067,1629430808,1629404002,1629396500,1629173017,1629140041,1629064008,1629019893,1629017287,1628972022,1628588292,1628541877,1628503043,1628413210,1628401478,1628355617,1628320608,1628319576,1628220856,1628191875,1628107370,1627917210,1627608268,1627364867,1627203601,1627198170,1627197720,1627185828,1627158298,1627117129,1627116029,1627016595,1626604476,1626512265,1626418240,1626417309,1625994002,1625976042,1625899323,1625655980,1625654001,1625636113,1625553037,1625472860,1625469473,1625311179,1625299966,1625145047,1625137627,1625133178,1624948061,1624872652,1624792442,1624784409,1624694892,1624521308,1624179604,1624170984,1624158022,1624096126,1624010411,1623997368,1623832144,1623827394,1623810742,1623746465,1623746169,1623744001,1623743669,1623743616,1623645069,1623574885,1623574885,1623574789,1623571204,1623480358,1623475245,1623394454,1623226431,1623043699,1622970007,1622970002,1622947767,1622940481,1622887212,1622883785,1622800813,1622800762,1622714412,1622696103,1622667888,1622532070,1622448519,1622435043,1622365202,1622361613,1622352482,1622345244,1622339298,1622332870,1622306919,1622273959,1622247038,1622108914,1622005646,1622003507,1621981037,1621940872,1621936973,1621919534,1621852996,1621833512,1621813366,1621741744,1621674009,1621668463,1621658162,1621584007,1621571246,1621556045,1621503936,1621490840,1621409717,1621326561,1621155601,1621153876,1621070316,1621070315,1620964494,1620890778,1620805638,1620720009,1620719782,1620719458,1620617058,1620554332,1620550802,1620541630,1620448082,1620343264,1620283637,1620283618,1620275530,1620273547,1620253474,1620212653,1620192536,1620186052,1620123945,1620028803,1620028803,1620020152,1620015215,1620010868,1619949611,1619940525,1619859641,1619859083,1619858409,1619780135,1619773201,1619760056,1619758810,1619738632,1619678896,1619668146,1619650272,1619595345,1619557678,1619554709,1619510614,1619479032,1619463348,1619432538,1619401262,1619378153,1619341223,1619339851,1619339350,1619336326,1619333160,1619330684,1619314832,1619313735,1619269212,1619254744,1619250925,1619250480,1619249676,1619246253,1619245347,1619227648,1619175601,1619172115,1619172010,1619167439,1619164744,1619144806,1619085609,1619079061,1619010007,1618991969,1618987228,1618984554,1618932131,1618911890,1618910243,1618893025,1618831076,1618750139,1618747122,1618746489,1618746138,1618744197,1618742652,1618741953,1618738127,1618736412,1618728457,1618723849,1618723816,1618660803,1618653567,1618650012,1618650001,1618601652,1618480810,1618457393,1618441091,1618435423,1618431324,1618412912,1618218020,1618131605,1618051383,1618004756,1617942782,1617930276,1617925797,1617923793,1617787867,1617703940,1617702450,1617609981,1617589322,1617523252,1617523203,1617476624,1617440407,1617379519,1617269198,1617235395,1617171110,1617094100,1617087399,1617080808,1617070277,1617053104,1617046293,1617009702,1616939669,1616922004,1616920615,1616918404,1616912161,1616846414,1616835611,1616835001,1616833187,1616829642,1616758588,1616757330,1616752859,1616749201,1616746054,1616560601,1616531674,1616491516,1616490412,1616490009,1616383767,1616383097,1616369505,1616312862,1616312193,1616246275,1616237754,1616232782,1616208322,1616188580,1616158812,1616115876,1616058014,1615987591,1615972177,1615971591,1615960981,1615958378,1615925086,1615885564,1615860336,1615719600,1615719193,1615712403,1615707118,1615687011,1615685570,1615625994,1615625970,1615602444,1615554008,1615521833,1615508483,1615439428,1615430299,1615409406,1615363206,1615274695,1615271784,1615258877,1615196615,1615107604,1615107604,1615104034,1615035609,1615010375,1614991424,1614987377,1614931201,1614838870,1614765569,1614711366,1614711157,1614693607,1614663074,1614589214,1614589203,1614588888,1614588145,1614520746,1614409787,1614386528,1614348006,1614157201,1614153113,1614148811,1614067207,1613984410,1613899286,1613898022,1613898008,1613897172,1613895902,1613895509,1613870256,1613862427,1613811602,1613810436,1613808550,1613808018,1613808005,1613806816,1613806563,1613698942,1613684450,1613656805,1613645454,1613642409,1613551230,1613484005,1613466014,1613392876,1613311205,1613268781,1613224804,1613221217,1613206397,1613203352,1613143317,1613138405,1613126114,1613098967,1613096149,1613072581,1613067181,1613066082,1613052005,1613042544,1613036419,1613036309,1613015497,1612972124,1612962010,1612939453,1612937040,1612927257,1612925279,1612918132,1612910737,1612901256,1612900975,1612879205,1612869964,1612862922,1612858063,1612857611,1612855789,1612853872,1612829544,1612793741,1612792805,1612784174,1612766805,1612763454,1612677600,1612610636,1612610300,1612609894,1612605603,1612539053,1612538585,1612538365,1612538051,1612537796,1612530016,1612515611,1612444803,1612444729,1612359302,1612357401,1612351112,1612349981,1612322066,1612318102,1612271294,1612271251,1612270916,1612260472,1612171033,1611987719,1611983650,1611973215,1611969219,1611829440,1611393947,1611391776,1611387906,1611379399,1611378813,1611367690,1611363694,1611221308,1611215290,1610959126,1610951928,1609143660,1609045625,1608462012,1608461349,1608456443,1608448699,1608343320,1607932198,1607154834,1606936275,1606906168,1606300743,1606296589,1605693611,1605006429,1605003972,1605001650,1604998512,1604918143,1604866369,1604664010,1604563204,1604224810,1603274413,1603048169,1602921606,1601896772,1599811369,1599730990,1599723894,1599716865,1598349603,1596535203,1596103206,1596016154,1595999047,1595984994,1595934266,1595930502,1595923480,1595919949,1595918459,1595781624,1595514742,1595499903,1595445714,1595413852,1595384960,1594514169,1594446823,1594429163,1594365340,1594364841,1594363746,1594344504,1594254205,1594220186,1594187278,1594114483,1594107231,1594105560,1594101494,1594014343,1594000261,1593949700,1593946895,1593935399,1593849622,1593848616,1593840702,1593805325,1593331209,1592208024,1592140397,1590825614,1590739186,1590480007,1588590125,1588498201,1598430896,1598430722,1598418104,1598349603,1598259794,1598248404,1598247689,1598086073,1598078123,1597973285,1597915279,1597908000,1597897361,1597890765,1597626797,1597622327,1597620094,1597559057,1597550647,1597547374,1597470573,1597364917,1597317979,1597226733,1597224833,1597209258,1597206364,1597205586,1597172153,1597120742,1597114850,1597112035,1597054621,1597020358,1597018679,1597017392,1597011868,1596971375,1596926033,1596924602,1596881918,1596791882,1596790770,1596789028,1596617725,1596605475,1596541122,1596535206,1596535203,1596448017,1596430819,1596420493,1596366744,1596362156,1596355212,1596303912,1596103833,1596103219,1596016154,1595999047,1595993331,1595984994,1595934266,1595930502,1595923480,1595919949,1595918459,1595781624,1595581212,1595577585,1595514742,1595499903,1595445709,1595413852,1595404857,1595384960,1595336674,1595318411,1595309559,1595307977,1595225139,1595160081,1595143056,1595122769,1595055389,1595048809,1595046647,1595030595,1594967143,1594899169,1594893608,1594893602,1594768666,1594715988,1594704672,1594701675,1594626927,1594514164,1594502320,1594446823,1594429158,1594365340,1594364834,1594363679,1594344504,1594254205,1594220186,1594187278,1594114483,1594108807,1594107231,1594105458,1594101494,1594014343,1594000261,1593949700,1593946890,1593935399,1593849622,1593848605,1593840702,1593805325,1593773403,1593745213,1593671953,1593666506,1593660263,1593653032,1593576003,1593573129,1593495336,1593417626,1593414477,1593413280,1593406938,1593393655,1593331208,1593331207,1593325416,1593321857,1593231840,1593167960,1593165586,1593072229,1593070254,1593063767,1592993426,1592964253,1592903760,1592891384,1592648827,1592621322,1592547895,1592522186,1592470352,1592439880,1592294410,1592289624,1592278220,1592267944,1592208024,1592201343,1592192741,1592180810,1592121608,1592035218,1591253986,1591084826,1590825615,1590823945,1590739206,1589889606,1589878803,1589457605,1589356673,1589181432,1588590083,1588590075,1588498201,1587732304,1587546036,1587470405,1587369607,1587286803,1586937406,1586854802,1586750332,1586743051,1586509201,1586505605,1586505504,1586253613,1586253605,1585987104,1585908054,1585814405,1585713532,1585630807,1585209585,1585123061,1585036769,1584777610,1584751218,1584604717,1584529213,1584529203,1584435602,1584431701,1584345595,1584273613,1584010817,1583754645,1583665186,1582011423,1582002709,1581903211,1581595209,1581503073,1581496032,1581471934,1581422407,1581336014,1581076808,1580385603,1580376584,1580374806,1579507235,1579342897,1579172418,1579158007,1578830411,1578739225,1578650409,1578560411,1578554999,1578549613,1578474356,1577585601,1577089765,1576908004,1576746015,1576652405,1576303204,1576152007,1576130249,1575810111,1575547204,1575529212,1575432376,1575283805,1575280789,1575259526,1574856007,1574330411,1573808427,1573733220,1573624818,1573462795,1573282069,1572782707,1572686956,1572559697,1572426003,1572408580,1572343218,1572264004,1572166804,1572162964,1571997618,1571907620,1571743923,1571738424,1571734805,1571700206,1571699449,1571569204,1571387431,1571196538,1571140802,1571126426,1571046086,1571041776,1570870802,1570795211,1570677592,1570577253,1570536007,1570524865,1570421451,1570346272,1570235255,1570183323,1570101003,1570085985,1570010413,1569914190,1569834009,1569818150,1569661201,1569539030,1569488404,1569484799,1569398415,1569315602,1569229203,1569154327,1569049184,1568884789,1568883628,1568707207,1568545199,1568538002,1568444974,1568338960,1568278802,1568271593,1568197713,1568196004,1568030417,1568030405,1567996337,1567936802,1567764012,1567760403,1567587603,1567587590,1567584012,1567505434,1567418411,1567416421,1567411201,1567408661,1567405367,1567193874,1567154490,1567079203,1567072816,1566637203,1566637154,1566547841,1566475208,1566460869,1566381606,1566201610,1566201603,1566124987,1566032402,1566001888,1565946004,1565942405,1565870410,1565859606,1565784006,1565773335,1565697607,1565697606,1565600403,1565514002,1565442002,1565424037,1565341204,1565334020,1565251208,1565168398,1565152205,1565078407,1564990202,1564916403,1564912803,1564871368,1564822802,1564740001,1564660802,1564578001,1564534759,1564533831,1564383602,1564304403,1564304401,1564218002,1564135199,1564121550,1564101613,1564056008,1564056004,1564041642,1563956291,1563936894,1563936894,1563870091,1563782414,1563699601,1563526813,1563354008,1563278400,1563181207,1563094788,1563008404,1563008243,1562978924,1562919333,1562839206,1562835603,1562835601,1562673604,1562670017,1562564881,1562493596,1562490002,1562483862,1562403608,1562317232,1562313609,1562310001,1562058010,1561971570,1561937283,1561890233,1561813200,1561795243,1561774573,1561712425,1561636801,1561543199,1561539608,1561539601,1561464000,1561453218,1561449608,1561449604,1561369530,1561367421,1561366802,1561276797,1561271872,1561249792,1561194005,1561032005,1561021206,1560927601,1560855602,1560848400,1560844810,1560786470,1560754796,1560754765,1560672300,1560654684,1560589211,1560589190,1560508719,1560502808,1560427199,1560412795,1560361566,1560330001,1560247212,1560243603,1559984368,1559969997,1559865220,1559864505,1559853300,1559531677,1559480435,1559462409,1559454996,1559378186,1559285975,1559263268,1559262351,1559218369,1559188815,1559120412,1559116802,1559101319,1559086731,1559070458,1559026801,1559011479,1559002307,1558942288,1558807134,1558780874,1558771203,1558688409,1558684921,1558655862,1558651144,1558602008,1558602004,1558509319,1558416619,1558170003,1558169997,1558164609,1558079946,1558041101,1557997152,1557995350,1557730800,1557655201,1557651597,1557538124,1557478799,1557119720,1557054017,1557054006,1557046802,1556960401,1556701201,1556614800,1556528406,1556528397,1556521206,1556441999,1556355602,1556355599,1556274601,1556190921,1556103659,1556096400,1556010002,1556002836,1555750802,1555664401,1555585204,1555581571,1555496999,1555495201,1555412436,1555408808,1555243203,1555239654,1555232407,1555146008,1555145996,1554984004,1554973204,1554807586,1554804001,1554800403,1554719398,1554714000,1554712248,1554634850,1554631200,1554627601,1554541200,1554454818,1554377400,1554368408,1554355755,1554313423,1554289209,1554202779,1554177617,1554077695,1554012585,1553936402,1553917992,1553831996,1553804800,1553759214,1553754940,1553749051,1553670300,1553629550,1553604946,1553597995,1553595940,1553593268,1553590801,1553586227,1553562311,1553561513,1553560640,1553560280,1553504404,1553468495,1553425199,1553418000,1553331601,1553254218,1553250599,1553158800,1553072404,1552986000,1552906810,1552895337,1552857895,1552820412,1552820407,1552820366,1552808148,1552764452,1552730401,1552640408,1552634931,1552632849,1552615247,1552553026,1552547458,1552474802,1552436324,1552390203,1552383552,1552379570,1552378372,1552372504,1552325037,1552303437,1552283622,1552255355,1552246185,1552215618,1552157130,1552153457,1552125109,1552042811,1552033800,1552032037,1551862800,1551785412,1551774615,1551653398,1551593446,1551436117,1551434894,1551433441,1551430806,1551353400,1551348013,1551348005,1551268800,1551258002,1551252572,1551182400,1551180599,1551154611,1551085202,1550998811,1550912416,1550912394,1550750408,1550743205,1550739601,1550566824,1550489403,1550480409,1550397606,1550394004,1550311208,1550307605,1550230203,1550221311,1550145643,1550145642,1550127629,1550057401,1550052001,1549972798,1549792808,1549792798,1549614643,1549536304,1549533603,1549530003,1549393183,1549360820,1549268989,1549261319,1549188004,1549177442,1549101594,1549097987,1548741623,1548647272,1548583221,1548583193,1548500407,1548410418,1548406804,1548241203,1548237635,1547978423,1547978358,1547974802,1547805620,1547715621,1547715615,1547456412,1547373609,1547370026,1547283646,1547208017,1547190003,1546934400,1546930799,1546842433,1546768832,1546678803,1546585203,1546517407,1546517400,1546506003,1546415093,1546333208,1546326003,1546163404,1546160399,1546160399,1546144173,1546074626,1546074020,1545984006,1545980401,1545908564,1545908520,1545901195,1545823801,1545555594,1545375603,1545307202,1545296401,1545261280,1545134417,1545127206,1545116428,1545116426,1544950803,1544857228,1544777999,1544770798,1544598019,1544596414,1544527815,1544522425,1544519153,1544443199,1544432401,1544356800,1544353201,1544252415,1544180406,1544173201,1543906812,1543836605,1543744806,1543561219,1543482433,1543452808,1543309221,1543309200,1543302007,1543143617,1543042821,1542884401,1542870010,1542704401,1542697220,1542538804,1542367805,1542281399,1542279601,1542195011,1542106808,1542099600,1542099599,1542096000,1542092413,1542020402,1542006005,1541833231,1541766608,1541764810,1541764800,1541754078,1541678407,1541588402,1541584804,1541581316,1541505607,1541501216,1541487628,1541404804,1541332795,1541325620,1541239174,1541239167,1541228416,1541218743,1541057149,1540898963,1540882817,1540789206,1540728016,1540717506,1540630854,1540623613,1540466965,1540378815,1540278009,1540270800,1540205750,1540037109,1540018814,1539939637,1539862202,1539860113,1539774062,1539674999,1539673215,1539514811,1539428409,1539421207,1539255603,1539172803,1539154814,1539086399,1539082848,1539075605,1538996397,1538989199,1538825405,1538823626,1538737224,1538650777,1538564092,1538550022,1538479797,1538478005,1538370004,1538305222,1538303407,1538290806,1538218851,1538217006,1538132406,1538046007,1538031605,1538028009,1537874997,1537866002,1537855214,1537779602,1537772411,1537696809,1537682404,1537671681,1537614041,1537606858,1537603228,1537566467,1537565069,1537516821,1537516097,1537466404,1537431876,1537426809,1537230599,1537207922,1537194269,1537194266,1537167613,1536822015,1536651010,1536562807,1536559214,1536476434,1536469207,1536232503,1536231611,1536230041,1536224377,1536217205,1536040817,1535958014,1535695215,1535626863,1535626808,1535612408,1535522417,1535353209,1535281211,1534773111,1534582810,1534402805,1534219239,1534158084,1534143619,1534121047,1533884406,1533727803,1533625226,1533020393,1532858404,1532764843,1532761492,1532592031,1532502140,1532426413,1532259902,1532156425,1532087101,1532000703,1531914303,1531897232,1531825219,1531727987,1531638024,1531566008,1531378812,1531314447,1531220408,1531119611,1531047606,1530874807,1530784811,1530687618,1530439198,1530342016,1529996412,1529840704,1529830823,1529830802,1529737209,1529731115,1529667902,1529658111,1529568766,1529495102,1529485210,1529478017,1529408702,1529394832,1529322303,1529235902"
pump_symbol_list = 'ATM,ASR,POWR,VIB,NEBL,ATM,PIVX,POWR,PNT,RAMP,TCT,OG,AGIX,CTXC,NEBL,CREAM,RDN,RAMP,AST,SNT,NXS,AST,TCT,QLC,SNM,GRS,ADX,NEBL,NXS,ELF,QSP,VIB,ALPHA,VIB,PHB,GRS,FXS,VIB,FOR,GXS,NXS,TKO,ELF,NAV,MDA,REQ,ACM,MODEFI,ARDR,PIVX,NXS,RAMP,APPC,NXS,NAS,EVX,ATM,ASR,NAS,CWAR,EVX,OAX,SUPER,EPS,VIB,VIB,MTH,NXS,NULS,QSP,BRD,REQ,BEL,FIRO,MTH,OAX,CHR,VIB,EZ,BRD,DUSK,NEBL,RDN,NXS,VIB,ARDR,GRS,SC,VIB,EVX,IDEX,FOR,VIB,SNT,ADX,AGIX,POA,EVX,NXS,RDN,BRD,AVAX,BEAM,ANT,WAXP,IRIS,GXS,PNT,IRIS,WABI,GXS,POND,BRD,SKL,VIB,VIB,WNXM,VIB,VIB,NXS,POA,ADX,NAV,SKY,VIB,QSP,ACM,ANT,BTCST,QLC,SKY,GTO,EZ,EVX,GXS,QLC,YOYO,APPC,MTH,SUPER,FIO,NXS,EVX,PNT,NEBL,NAV,FXS,BRD,AION,CTXC,PIVX,CHZ,RDN,GTO,DLT,ROSE,PHB,ALGO,QLC,AVAX,OAX,SOL,FUN,NEAR,ADX,ALGO,SFP,DOGE,NXS,VIB,MDA,PNT,ALPHA,CHZ,SKL,BRD,ICP,BNB,KEEP,GXS,QSP,BLZ,TCT,SRM,NAS,POND,GVT,FOR,AION,WRX,ARPA,NU,FOR,OAX,CTXC,ADX,BEAM,RDN,MDA,ARPA,ARPA,EZ,AVAX,APPC,ANKR,CTXC,BRD,LSK,EVX,BTS,NEBL,ARPA,DREP,EVX,NXS,QLC,FOR,GRS,GVT,POA,FOR,REQ,CTSI,TRU,POA,OAX,VIA,FIS,EZ,ARPA,TWT,MDA,NEBL,YOYO,IDEX,LINK,QSP,DLT,OAX,ARPA,DOGE,MTH,ADX,ELF,WABI,TRU,NAV,VIA,NVC,CDT,NAS,ARK,SXP,CTXC,ONE,REP,RLC,OST,MATIC,DLT,FIO,LIT,QSP,GVT,YOYO,POA,QLC,WABI,CND,MTH,POA,ELF,ACM,YOYO,ECN,MTL,IN,ENJ,REEF,EOS,SNT,BAL,OAX,DLT,APPC,PIVX,BRD,NXS,YES,OAX,SKY,NEBL,OAX,TVK,NAV,POA,APPC,OST,NAS,BADGER,WPR,IDEX,EVX,NEAR,SKY,NEBL,BLZ,ELF,REEF,ICX,MATIC,ELF,DLT,LOOM,DATA,CTXC,CTXC,AMB,PHA,QLC,EVX,NXS,MDA,CND,WPR,ELF,ORN,AST,SKL,XRP,1INCH,ONE,ELF,XEM,COTI,DOGE,FXS,DLT,DLT,DLT,BLZ,LSK,BRD,AGI,DLT,NXS,ELF,AMB,CFX,PHA,BRD,MDA,BAL,BTG,FXS,REEF,BADGER,FIS,OAX,AST,APPC,NAS,BEAM,VIB,IDEX,DOGE,DOGE,ACM,CDT,ELF,GRS,MDA,RDN,DLT,DLT,DUSK,BRD,APPC,ONG,LINK,CND,DOGE,HAC,RDN,VIB,DLT,IN,ACM,VIA,WPR,POWR,SKY,NEBL,LINK,LINA,EGLD,NXS,BNB,XTZ,SC,DOGE,DOGE,LTO,CHZ,ETC,PAXG,BNB,DOGE,VET,RCN,APPC,ASR,OG,CTXC,CDT,BAND,ELF,NAV,WABI,APPC,ONG,VIA,NEBL,ARPA,ROSE,FIL,DEGO,LINA,SUSD,STRAX,ACM,KAVA,SXP,CTXC,VIA,AST,ASR,LSK,EOS,POWR,BTG,STORJ,NEAR,OM,STRAX,ANT,WAN,REEF,PIVX,PIVX,ATM,LRC,WNXM,GVT,ATM,NAV,VIA,STEEM,COTI,VIA,NMR,NAV,MATIC,REQ,AST,WTC,ONT,APPC,POWR,AST,KNC,IDEX,LINK,DEGO,NAV,ZRX,MDT,AST,MAN,GTO,CTXC,ZRX,STEEM,VIA,SXP,MATIC,TROY,ADA,AST,RDN,PSG,NAV,MDT,POND,SKL,VIA,ASR,ADA,TTU,OCEAN,CHZ,BLZ,NAS,REEF,NXS,AST,YOYO,ANT,ETH,PPT,PPT,BTS,LKY,PPT,SC,WABI,GRS,UMA,ELF,POWR,IRIS,NEXO,ANT,MTH,MTH,PSG,OG,ROBET,ADA,ARK,SUSHI,BRD,CTXC,GXS,CDT,RDN,STPT,PIVX,NXS,PNT,ETH,ETH,CTK,NXS,GVT,WPR,COTI,SKY,PNT,SKY,NEBL,FIO,EOS,LPT,WABI,WPR,EGLD,RTH,VIB,REEF,EURS,WAVES,UGAS,NEBL,DASH,ADX,EOS,BRC,POWR,TCT,REEF,EOS,XRP,PNT,DTX,EOS,CRV,DOGE,REEF,BLZ,MDA,CTSI,WAN,XRP,EOS,MDT,BEL,WAN,IRIS,HXRO,MDT,EOS,TROY,ARDR,MDT,NEO,ADA,HIVE,WTP,XVG,DOGE,DOGE,GVT,DOGE,ADA,ETH,BRD,TRX,ZRX,LIT,EOS,VET,VIB,APPC,SKY,EOS,DOGE,SKY,TRU,STEEM,EOS,STMX,GRT,WING,ETH,WABI,ONT,VIA,ARK,FOR,CDT,NBS,ARK,WABI,VIA,BCPT,NXS,RDN,EVX,NAS,APPC,OXT,BEAM,GXS,APPC,NAV,MBL,DGB,LSK,HC,COS,NAV,BCPT,DLT,BCPT,APPC,APPC,STEEM,GXS,NAV,MTL,IOST,CTXC,NXS,OAX,YOYO,PPT,STMX,RDN,TCT,SNT,DNT,ADA,TROY,RDN,PPT,VIB,APPC,OST,BTS,CVC,STPT,CTXC,POLY,MATIC,MTH,VIA,MANA,STMX,TNT,STEEM,MITH,KMD,WRX,NXS,CTXC,NAS,POWR,EVX,OMG,BLZ,GNT,CTXC,SYS,BQX,STORJ,ARN,WTC,ARDR,REQ,GVT,HC,STPT,INS,OAX,GXS,NEBL,NAS,VIA,ONG,MDA,PPT,LSK,VIA,ONT,RDN,CHR,MITH,WAVES,XEM,AE,GAS,STORJ,NXS,OST,WPR,TCT,QTUM,POWR,BCPT,TFUEL,SNGLS,SC,ZRX,CVC,MTH,APPC,SNM,WPR,PHB,WRX,VIA,TFUEL,STMX,QTUM,WABI,BTS,WAN,NANO,SNGLS,LSK,QTUM,MTL,AION,GXS,GXS,BOA,CTXC,BAT,PPT,PPT,PIVX,BAND,PPT,XEM,MBL,NXS,ETH,DOGE,VIB,APPC,OST,MBL,BTS,CVC,STPT,CTXC,POLY,MATIC,MTH,ELF,WAN,VIA,MANA,STMX,TNT,SNT,STEEM,LTO,NXS,OAX,QSP,POWR,INS,SYS,ONG,STX,QSP,INS,WTC,PIVX,HC,SYS,SYS,CVC,SKY,POA,POA,SNM,MITH,IOTX,KMD,WRX,NXS,CTXC,NAS,POWR,EVX,OMG,BLZ,GNT,ADX,CTXC,SYS,BQX,STORJ,ARN,WTC,ARDR,REQ,GVT,HC,STPT,INS,LTC,NXS,AION,TFUEL,BTS,GAS,XLM,GAS,EVX,QSP,GRS,CTXC,NAV,NXS,OAX,OAX,ADX,LUN,ELF,NKN,SYS,AMB,STPT,OAX,NEBL,PPT,VIA,NEBL,SYS,WAN,SYS,NEBL,VIA,ONG,HC,PIVX,SKY,GVT,GXS,BCPT,BCPT,CTXC,NEBL,QSP,OAX,ARK,NAS,GXS,VIA,MORE,LOOM,SIB,ZIL,WATER,MDA,MDA,PPT,DLT,AOA,MORE,RLC,WPR,GVT,SNT,VITE,NKN,WPR,GNT,ELF,ARN,ARN,GVT,ARK,GRS,SNGLS,NEBL,EDO,NXS,BRD,TNB,MTH,STORJ,LUN,LUN,RLC,BNT,NAV,NEBL,POA,NAV,SNGLS,KAVA,KAVA,XTZ,MORE,RDN,FTM,FET,QKC,WPR,PPT,VRC,NXS,NULS,BRD,NULS,NAV,PPT,VIB,ARDR,GNT,ONG,OST,QKC,EDO,IN,BRD,FTM,NAV,REN,FTM,CURE,DUSK,EDO,MDA,MDA,BEAM,CDT,NAS,CDT,MORE,EDO,BNT,PINK,MDA,BCD,POA,QKC,DGD,ONE,QKC,GRS,ONG,UP,MDA,NEBL,NEBL,MDA,IN,OST,FUN,XRP,XRP,MDA,EDO,NULS,RDN,GRS,SNGLS,BNT,BLZ,PPT,AE,POWR,PPT,BRD,LSK,NAV,CHZ,AST,BAT,BRD,NXS,CMT,MDA,CMT,FUN,MITH,GVT,BLZ,EDO,BAT,MANA,DCR,INS,ONG,ONG,BLZ,APPC,QKC,MDA,BRD,LINK,ARK,RLC,QKC,BNT,BNT,MATIC,DATA,EDO,MTH,SNM,POA,QLC,FTM,GVT,RLC,LRC,RLC,MTH,KMD,WAN,QSP,QSP,GVT,POWR,OST,SNT,BTS,VIB,QLC,ONG,GXS,TFD,CDT,DLT,VIA,DATA,DLT,FUN,ALGO,CVC,CVC,WPR,MANA,DLT,RCN,MANA,CDT,YOYO,SNM,ENG,POA,WPR,QKC,SNM,QKC,FUN,WABI,NAV,BNT,ELF,ICX,RDN,BLZ,QKC,MATIC,ADX,ARN,NULS,LRC,LRC,APPC,NEO,NEO,EOS,GRS,SNT,FUN,BTS,SYS,MTH,DLT,VIA,BLZ,NAV,REQ,WABI,BNT,FUN,SNM,GEO,SPX,DENT,SYS,PPT,QSP,FUN,ADX,PIVX,QSP,VIB,REQ,REN,FUN,REN,DNT,CDT,SNGLS,NLG,MTH,PPT,DNT,GRC,BAT,INS,OAX,SNGLS,APPC,NAV,INK,APPC,CND,BLZ,PINK,PAX,REN,ERT,LEND,BNT,IOTX,NXS,BRD,LEND,AMB,LEND,BNT,AST,PPT,IOC,CDT,ARDR,DLT,STORJ,PAX,REN,REQ,POWR,CVC,TNB,WPR,SNM,PIVX,THETA,DLT,PPT,EVX,MITH,BOXX,MTH,QKC,MANA,POLY,ONG,DNT,QSP,DNT,QKC,DATA,DATA,WABI,BRD,CRPT,FET,ELF,GNT,CAG,PAX,BRD,CND,PAX,NAV,HC,CDT,MATIC,HC,MTH,CDT,VERI,HC,RDN,PAX,BCPT,POA,TFD,ENJ,PPT,PPT,BLZ,BLZ,BLZ,REQ,CTXC,UKG,WTL,TALK,ADX,APPC,RDN,ENJ,SNM,STORM,PPT,FTM,POLL,ASCS,PPT,VIBE,FTM,C20,BRD,DAI,BNT,BLZ,MET,SNM,RDN,LEND,QKC,DOX,PPT,NEBL,DLT,LINK,AOA,BNT,HQX,GBG,BNT,SNM,IOTX,VERI,CND,PTOY,DATA,STORJ,TFD,ARDR,DNT,MITH,WABI,AMB,LRC,NAS,BCPT,MTH,BRD,PROFIT,AGI,HQX,VIA,REN,BAT,EVX,QLC,DADI,GTO,REN,HQX,FC,CTXC,FC,DADI,ING,REN,CDT,VIBE,ZIL,LEND,VERI,BRD,BNT,BTT,ING,ENJ,BLZ,RLC,ARDR,BCHSV,DCR,SWM,AGI,M1,EDO,NANO,RLC,DCR,THETA,MCO,ARK,TUSD,VIB,OAX,BNT,BAT,BNT,LEND,AMB,POLY,THETA,CROC,GRS,LOOM,MDA,DATA,DATA,DATA,CRPT,ASCS,EVX,REN,BLZ,SYS,BRD,BRX,FC,STEEM,STORJ,BQX,UKG,HC,GBG,LEND,STORJ,BLZ,TKN,WTC,FTM,UKG,EDO,AOA,PIE,DADI,LEND,LEND,REQ,DOX,TFD,GAM,CHP,GXS,SUB,KMD,WPR,THETA,BTT,CDT,STORJ,WTC,WPR,VIA,GRS,RDN,BQX,WINGS,LEND,WINGS,REN,ENJ,WTC,TNT,ZIP,FTEC,GXS,VIA,TDH,REN,REN,MTH,DARK,THETA,OK,BBT,UTC,EVX,BBT,LOOM,APX,KMD,RNS,DZC,DZC,WTC,BRD,TNT,CHESS,WPR,BRD,BRD,BQX,ARN,BNT,QKC,MATRX,BSV,BAT,HC,GRW,NEBL,RIYA,XBP,MTH,FUZZ,TIX,LOOM,FUZZ,ETT,WABI,CON,XPTX,FUEL,ETT,REN,RIYA,ZRX,NPXS,ONT,EVX,ARCO,EQT,HAC,PLR,OAX,DZC,CHESS,XZX,MBRS,NCASH,FTC,BSV,RDN,OSC,OSC,QBT,QBT,MOD,EVX,CXT,FROST,CON,UMO,MBRS,BVB,OSC,BRD,BRD,MAGN,CTIC3,FLAX,VIA,FLAX,BLOCK,ZNY,ZNY,ALIS,DUO,BSTY,EVX,WINGS,BCS,OST,TIX,KOBO,FLAX,CNO,OXY,OXY,DRPU,LINK,FONZ,ETT,TAJ,EXCL,GNO,RDN,ALIS,HAC,XPTX,GRS,FLAX,DYN,SKRL,XZC,PCOIN,UFR,XID,TAJ,POLY,GRW,DRXNE,ALL,EDO,SRN,MAC,C2,SKR,CQST,OAX,CHAN,KING,FUZZ,DOPE,EVX,FROST,BRD,BCH,BEEZ,IVY,EGC,GNO,VIA,CAN,KING,DATA,OXY,PEPE,SYNX,MATRX,HC,SPR,SPR,OAX,AUR,WSP,SIB,MST,STORM,NAV,ALIS,SUB,BAT,BLZ,XPRO,ENG,WW,ARN,SPR,GRS,GRS,TRX,LTC,UBT,EVO,ICN,FUZZ,DNT,MATRX,ALEX,BNC,CMT,GRS,GRS,ERY,SRC,BDL,CAT,FLAX,ELM,GRN,EVIL,BERN,SHRM,ETC,CACH,ARI,UKG,COAL,BEEZ,TX,FC2,INPAY,ELM,EDC,MNE,HAC,FC2,SLING,BEEZ,MAGN,PNC,KRONE,TEC,BXT,NPC,CON,EUC,SNPT,GUN,OSC,QBT,FNTB,BUBO,SPT,RIYA,ZNY,EBG,TRK,SNPT,CQST,RBT,GET,SIG,CC,BVB,NLC2,KTK,MTH,PIVX,RLT,CHP,TRK,WIT,XVG,RR,BNBX'


import argparse
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

if __name__ == "__main__":

    # connect influxdbSYNCHRONOUS
    bucket_trades = "Klines"
    client = InfluxDBClient(
        url="http://localhost:8086",
        token=
        "-vKh8eaHviakWO6CO7CP4AsJAcK7WF845TcCb4mHz22SsYdW0JQ6HtQJ1kwun8eoFC4ariy_SHVquwsMy3nw5Q==",
        org="NUS")

    write_api = client.write_api(write_options=SYNCHRONOUS)
    query_api = client.query_api()

    #
    pump_time_list = pump_time_list.split(",")
    pump_symbol_list = pump_symbol_list.split(",")
    interval = 60

    for i in range(len(pump_symbol_list)):

        pump_time = int(pump_time_list[i])
        symbol = pump_symbol_list[i] + "_USDT"

        starts = []
        prices = []
        volumes = []

        try:
            start = pump_time - interval - 1
            stop = pump_time + interval - 1

            q_str = '''from (bucket: "{}") |> range(start: {}, stop: {})'''.format(
                bucket_trades, start, stop)
            q_str += '''|> filter (fn: (r) => r["_measurement"] == "{}")'''.format(
                symbol)
            q_str += '''|> filter(fn: (r) => r["_field"] == "high" or r["_field"] == "low" or r["_field"] == "volume")'''
            q_str += '''|> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")'''

            tables = query_api.query(q_str)

            if len(tables)>0:
                print(pump_symbol_list[i] +" in the database")

            else:
                print(pump_symbol_list[i] +" not found..")

        except Exception as e:
            print(e)

