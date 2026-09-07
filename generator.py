import os
from datetime import datetime

# 1. 사이트 기본 설정
DOMAIN = "https://offmoderapy.netlify.app"
SITE_NAME = "오프모드건마사랑"
NAVER_VERIFICATION = "a0e02e4f2dcaf270179e713519c690fbe449e8c5"

# 2. 제휴 업체 정보 데이터 (5개 업체)
PARTNER_SHOPS = [
    {"name": "퀸즈홈테라피", "tel": "0507-1280-3296", "desc": "프리미엄 맞춤 홈케어 및 스웨디시 전문"},
    {"name": "한국골든테라피", "tel": "0507-1280-3360", "desc": "정통 힐링 아로마 및 전신 관리"},
    {"name": "한국미인테라피", "tel": "0507-1280-3201", "desc": "편안하고 아늑한 1:1 맞춤 케어"},
    {"name": "오늘밤테라피", "tel": "0507-1280-3199", "desc": "24시 신속 방문 및 피로 회복 전문"},
    {"name": "주주테라피", "tel": "0507-1280-3197", "desc": "감성 힐링 및 전문 테라피 복합 코스"}
]

# 3. 서울특별시 25개 구 및 법정동 데이터
seoul_regions = {
    "jongno": {"name": "종로구", "dongs": ["청운동", "신교동", "궁정동", "효자동", "창성동", "통인동", "누상동", "누하동", "옥인동", "체부동", "통의동", "사직동", "도렴동", "당주동", "내수동", "신문로1가", "신문로2가", "세종로", "종로1가", "종로2가", "종로3가", "종로4가", "종로5가", "종로6가", "이화동", "연건동", "충신동", "동숭동", "혜화동", "명륜1가", "명륜2가", "명륜3가", "명륜4가", "창신동", "숭인동", "효제동", "가회동", "삼청동", "안국동", "익선동", "낙원동", "돈의동", "장사동", "관수동", "인사동", "원서동", "제동", "계동", "화동", "팔판동", "묘동", "봉익동", "와룡동", "권농동", "서린동", "수송동", "견지동", "공평동", "관철동"]},
    "jung": {"name": "중구", "dongs": ["무교동", "다동", "태평로1가", "태평로2가", "남대문로1가", "남대문로2가", "남대문로3가", "남대문로4가", "남대문로5가", "봉래동1가", "봉래동2가", "회현동1가", "회현동2가", "회현동3가", "충무로1가", "충무로2가", "충무로3가", "충무로4가", "충무로5가", "명동1가", "명동2가", "필동1가", "필동2가", "필동3가", "주교동", "방산동", "오장동", "입정동", "산림동", "초동", "을지로1가", "을지로2가", "을지로3가", "을지로4가", "을지로5가", "황학동", "서소문동", "정동", "순화동", "중림동", "신당동", "흥인동", "무학동", "상왕십리동", "하왕십리동", "광희동1가", "광희동2가", "쌍림동", "장충동1가", "장충동2가"]},
    "yongsan": {"name": "용산구", "dongs": ["후암동", "용산동1가", "용산동2가", "용산동3가", "용산동4가", "용산동5가", "용산동6가", "동빙고동", "서빙고동", "주성동", "보광동", "한남동", "이태원동", "서계동", "청파동1가", "청파동2가", "청파동3가", "원효로1가", "원효로2가", "원효로3가", "원효로4가", "효창동", "용문동", "도원동", "마포동", "한강로1가", "한강로2가", "한강로3가", "이촌동", "신계동", "문배동", "신창동", "산천동", "청암동"]},
    "seongdong": {"name": "성동구", "dongs": ["상왕십리동", "하왕십리동", "홍익동", "도선동", "마장동", "사근동", "행당동", "응봉동", "금호동1가", "금호동2가", "금호동3가", "금호동4가", "옥수동", "성수동1가", "성수동2가", "송정동", "용답동", "왕십리동"]},
    "gwangjin": {"name": "광진구", "dongs": ["화양동", "군자동", "중곡동", "능동", "광장동", "자양동", "구의동", "자양1동", "자양2동", "자양3동", "자양4동", "구의1동", "구의2동", "구의3동", "중곡1동", "중곡2동", "중곡3동", "중곡4동"]},
    "dongdaemun": {"name": "동대문구", "dongs": ["신설동", "용두동", "제기동", "청량리동", "회기동", "휘경동", "이문동", "전농동", "답십리동", "장안동", "전농1동", "전농2동", "답십리1동", "답십리2동", "장안1동", "장안2동"]},
    "jungnang": {"name": "중랑구", "dongs": ["면목동", "상봉동", "중화동", "묵동", "망우동", "신내동", "면목본동", "면목2동", "면목3동", "면목4동", "면목5동", "면목7동", "상봉1동", "상봉2동", "중화1동", "중화2동", "묵1동", "묵2동", "망우본동", "망우3동", "신내1동", "신내2동"]},
    "seongbuk": {"name": "성북구", "dongs": ["성북동", "동소문동1가", "동소문동2가", "동소문동3가", "동소문동4가", "동소문동5가", "동소문동6가", "동소문동7가", "삼선동1가", "삼선동2가", "삼선동3가", "삼선동4가", "삼선동5가", "동선동1가", "동선동2가", "동선동3가", "동선동4가", "동선동5가", "보문동1가", "보문동2가", "보문동3가", "보문동4가", "보문동5가", "보문동6가", "정릉동", "길음동", "종암동", "하월곡동", "상월곡동", "장위동", "석관동", "돈암동", "안암동"]},
    "gangbuk": {"name": "강북구", "dongs": ["미아동", "번동", "수유동", "우이동", "삼양동", "송천동", "삼각산동", "인수동"]},
    "dobong": {"name": "도봉구", "dongs": ["창동", "도봉동", "방학동", "쌍문동", "방학1동", "방학2동", "방학3동", "쌍문1동", "쌍문2동", "쌍문3동", "쌍문4동", "창1동", "창2동", "창3동", "창4동", "창5동", "도봉1동", "도봉2동"]},
    "nowon": {"name": "노원구", "dongs": ["월계동", "공릉동", "하계동", "중계동", "상계동", "상계1동", "상계2동", "상계3동", "상계4동", "상계5동", "상계6동", "상계7동", "상계8동", "상계9동", "상계10동", "중계본동", "중계1동", "중계2동", "중계3동", "중계4동", "하계1동", "하계2동", "공릉1동", "공릉2동", "월계1동", "월계2동", "월계3동"]},
    "eunpyeong": {"name": "은평구", "dongs": ["불광동", "갈현동", "구산동", "대조동", "응암동", "역촌동", "신사동", "증산동", "수색동", "진관동", "녹번동", "불광1동", "불광2동", "갈현1동", "갈현2동", "응암1동", "응암2동", "응암3동", "신사1동", "신사2동"]},
    "seodaemun": {"name": "서대문구", "dongs": ["충정로동", "합동", "미근동", "냉천동", "천연동", "옥천동", "영천동", "현저동", "북아현동", "신촌동", "대현동", "창천동", "연희동", "홍제동", "홍은동", "남가좌동", "북가좌동", "홍제1동", "홍제2동", "홍제3동", "홍은1동", "홍은2동", "남가좌1동", "남가좌2동", "북가좌1동", "북가좌2동"]},
    "mapo": {"name": "마포구", "dongs": ["아현동", "공덕동", "신공덕동", "도화동", "용강동", "토정동", "마포동", "대흥동", "염리동", "노고산동", "신수동", "상암동", "중동", "성산동", "합정동", "서교동", "동교동", "망원동", "연남동", "창전동", "망원1동", "망원2동", "성산1동", "성산2동"]},
    "yangcheon": {"name": "양천구", "dongs": ["신정동", "목동", "신월동", "목1동", "목2동", "목3동", "목4동", "목5동", "신월1동", "신월2동", "신월3동", "신월4동", "신월5동", "신월6동", "신월7동", "신정1동", "신정2동", "신정3동", "신정4동", "신정6동", "신정7동"]},
    "gangseo": {"name": "강서구", "dongs": ["염창동", "등촌동", "화곡동", "가양동", "마곡동", "내발산동", "외발산동", "공항동", "방화동", "화곡본동", "화곡1동", "화곡2동", "화곡3동", "화곡4동", "화곡6동", "화곡8동", "우장산동", "발산1동", "방화1동", "방화2동", "방화3동"]},
    "guro": {"name": "구로구", "dongs": ["신도림동", "구로동", "가리봉동", "고척동", "개봉동", "오류동", "궁동", "항동", "천왕동", "시흥동", "구로1동", "구로2동", "구로3동", "구로4동", "구로5동", "개봉1동", "개봉2동", "개봉3동", "고척1동", "고척2동", "오류1동", "오류2동", "수궁동"]},
    "geumcheon": {"name": "금천구", "dongs": ["가산동", "독산동", "시흥동", "독산1동", "독산2동", "독산3동", "독산4동", "시흥1동", "시흥2동", "시흥3동", "시흥4동", "시흥5동"]},
    "yeongdeungpo": {"name": "영등포구", "dongs": ["영등포동", "여의도동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동", "영등포본동", "당산1동", "당산2동", "양평1동", "양평2동", "신길1동", "신길3동", "신길4동", "신길5동", "신길6동", "신길7동", "대림1동", "대림2동", "대림3동"]},
    "dongjak": {"name": "동작구", "dongs": ["노량진동", "상도동", "흑석동", "사당동", "대방동", "신대방동", "노량진1동", "노량진2동", "상도1동", "상도2동", "상도3동", "상도4동", "사당1동", "사당2동", "사당3동", "사당4동", "사당5동", "신대방1동", "신대방2동"]},
    "gwanak": {"name": "관악구", "dongs": ["봉천동", "신림동", "남현동", "보라매동", "청림동", "성현동", "행운동", "낙성대동", "청룡동", "은천동", "서원동", "신원동", "서림동", "신사동", "난향동", "조원동", "대학동", "삼성동", "난곡동"]},
    "seocho": {"name": "서초구", "dongs": ["서초동", "반포동", "방배동", "잠원동", "우면동", "원지동", "양재동", "내곡동", "신원동", "서초1동", "서초2동", "서초3동", "서초4동", "반포본동", "반포1동", "반포2동", "반포3동", "반포4동", "방배본동", "방배1동", "방배2동", "방배3동", "방배4동", "양재1동", "양재2동"]},
    "gangnam": {"name": "강남구", "dongs": ["역삼동", "논현동", "청담동", "삼성동", "대치동", "신사동", "도곡동", "개포동", "일원동", "수서동", "자곡동", "율현동", "세곡동", "압구정동", "논현1동", "논현2동", "삼성1동", "삼성2동", "대치1동", "대치2동", "대치4동", "역삼1동", "역삼2동", "도곡1동", "도곡2동", "개포1동", "개포4동", "일원본동", "일원1동", "일원2동"]},
    "songpa": {"name": "송파구", "dongs": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "장지동", "방이동", "오금동", "거여동", "마천동", "잠실본동", "잠실2동", "잠실3동", "잠실4동", "잠실6동", "잠실7동", "풍납1동", "풍납2동", "거여1동", "거여2동", "마천1동", "마천2동", "방이1동", "방이2동", "송파1동", "송파2동", "가락본동", "가락1동", "가락2동", "문정1동", "문정2동", "위례동"]},
    "gangdong": {"name": "강동구", "dongs": ["고덕동", "상일동", "명일동", "암사동", "천호동", "성내동", "둔촌동", "강일동", "상일1동", "상일2동", "명일1동", "명일2동", "고덕1동", "고덕2동", "암사1동", "암사2동", "암사3동", "천호1동", "천호2동", "천호3동", "성내1동", "성내2동", "성내3동", "둔촌1동", "둔촌2동", "길동"]}
}

# 4. 경기도 전체 시·군·구 데이터
gyeonggi_regions = {
    "suwon-jangan": {"name": "수원시 장안구", "dongs": ["파장동", "정자동", "이목동", "율전동", "천천동", "영화동", "조원동", "송죽동"]},
    "suwon-gwonseon": {"name": "수원시 권선구", "dongs": ["세류동", "평동", "호매실동", "곡선동", "권선동", "입북동", "서둔동"]},
    "suwon-paldal": {"name": "수원시 팔달구", "dongs": ["매교동", "매산동", "고등동", "화서동", "지동", "우만동", "인계동"]},
    "suwon-yeongtong": {"name": "수원시 영통구", "dongs": ["매탄동", "원천동", "영통동", "이의동", "하동", "망포동"]},
    "seongnam-sujeong": {"name": "성남시 수정구", "dongs": ["태평동", "신흥동", "수진동", "단대동", "산성동", "상적동", "시흥동", "신촌동", "오야동", "심곡동"]},
    "seongnam-jungwon": {"name": "성남시 중원구", "dongs": ["성남동", "중앙동", "금광동", "은행동", "하대원동", "도촌동", "여수동", "갈현동"]},
    "seongnam-bundang": {"name": "성남시 분당구", "dongs": ["분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "판교동", "삼평동", "백현동", "금곡동", "구미동", "운중동", "대장동"]},
    "goyang-deokyang": {"name": "고양시 덕양구", "dongs": ["원신동", "효자동", "삼송동", "화정동", "행신동", "성사동", "고양동", "능곡동", "주교동", "대덕동", "흥도동", "창릉동"]},
    "goyang-ilsandong": {"name": "고양시 일산동구", "dongs": ["식사동", "중산동", "정발산동", "백석동", "마두동", "장항동", "풍동", "고봉동", "사리현동", "설문동"]},
    "goyang-ilsanseo": {"name": "고양시 일산서구", "dongs": ["일산동", "주엽동", "탄현동", "대화동", "가좌동", "송포동", "덕이동", "법곳동"]},
    "yongin-cheoin": {"name": "용인시 처인구", "dongs": ["포곡읍", "모현읍", "역삼동", "유림동", "동부동", "남사읍", "원삼면", "백암면", "양지면"]},
    "yongin-giheung": {"name": "용인시 기흥구", "dongs": ["신갈동", "기흥동", "서농동", "구성동", "마북동", "동백동", "보정동", "상갈동", "영덕동"]},
    "yongin-suji": {"name": "용인시 수지구", "dongs": ["풍덕천동", "죽전동", "동천동", "상현동", "성복동", "신봉동", "고기동"]},
    "bucheon": {"name": "부천시", "dongs": ["원미동", "심곡동", "소사동", "중동", "상동", "역곡동", "소사본동", "괴안동", "범박동", "오정동", "내동", "삼정동"]},
    "ansan-sangrok": {"name": "안산시 상록구", "dongs": ["사동", "일동", "이동", "본오동", "반월동", "부곡동", "초지동", "성포동", "월피동"]},
    "ansan-danwon": {"name": "안산시 단원구", "dongs": ["고잔동", "와동", "선부동", "원곡동", "초지동", "대부동", "호수동", "백운동"]},
    "anyang-manan": {"name": "안양시 만안구", "dongs": ["안양동", "석수동", "박달동"]},
    "anyang-dongan": {"name": "안양시 동안구", "dongs": ["비산동", "관양동", "평촌동", "범계동", "호계동"]},
    "uijeongbu": {"name": "의정부시", "dongs": ["의정부동", "호원동", "가능동", "녹양동", "신곡동", "장암동", "송산동", "민락동", "금오동"]},
    "hwaseong": {"name": "화성시", "dongs": ["봉담읍", "향남읍", "매송면", "비봉면", "남양읍", "동탄동", "병점동", "반월동", "우정읍", "팔탄면", "정남면", "새솔동"]},
    "pyeongtaek": {"name": "평택시", "dongs": ["팽성읍", "안중읍", "포승읍", "진위면", "서정동", "송탄동", "중앙동", "고덕면", "청북읍", "비전동", "동삭동"]},
    "gwangmyeong": {"name": "광명시", "dongs": ["광명동", "철산동", "하안동", "소하동", "일직동"]},
    "siheung": {"name": "시흥시", "dongs": ["대야동", "신천동", "은행동", "목감동", "군자동", "정왕동", "배곧동", "장곡동", "능곡동"]},
    "paju": {"name": "파주시", "dongs": ["문산읍", "조리읍", "법원읍", "탄현면", "교하동", "금촌동", "운정동", "파주읍", "광탄면"]},
    "gimpo": {"name": "김포시", "dongs": ["통진읍", "고촌읍", "양촌읍", "사우동", "풍무동", "장기동", "운양동", "구래동", "마산동"]},
    "gwangju-si": {"name": "광주시", "dongs": ["오포읍", "초월읍", "곤지암읍", "도척면", "퇴촌면", "경안동", "송정동", "역동", "태전동"]},
    "hanam": {"name": "하남시", "dongs": ["천현동", "신장동", "풍산동", "미사동", "감일동", "위례동", "춘궁동", "덕풍동"]},
    "namyangju": {"name": "남양주시", "dongs": ["와부읍", "진접읍", "화도읍", "오남읍", "진건읍", "퇴계원읍", "호평동", "평내동", "다산동"]},
    "osan": {"name": "오산시", "dongs": ["중앙동", "세마동", "초평동", "대원동", "남촌동", "신장동"]},
    "icheon": {"name": "이천시", "dongs": ["마장면", "부발읍", "장호원읍", "중리동", "증포동", "창전동", "신둔면", "백사면"]},
    "guri": {"name": "구리시", "dongs": ["갈매동", "동구동", "인창동", "교문동", "수택동", "토평동"]},
    "pocheon": {"name": "포천시", "dongs": ["소흘읍", "군내면", "내촌면", "신북면", "포천동", "가산면", "창수면"]},
    "yangju": {"name": "양주시", "dongs": ["회천동", "장흥면", "은현면", "남면", "백석읍", "고읍동", "옥정동"]},
    "yeoju": {"name": "여주시", "dongs": ["가남읍", "점동면", "금사면", "여흥동", "중앙동", "오학동", "북내면"]},
    "dongducheon": {"name": "동두천시", "dongs": ["생연동", "보산동", "동두천동", "상패동", "송내동", "지행동", "소요동"]},
    "gwacheon": {"name": "과천시", "dongs": ["중앙동", "갈현동", "문원동", "별양동", "부림동", "과천동", "주암동"]},
    "gunpo": {"name": "군포시", "dongs": ["군포동", "금정동", "산본동", "대야동", "수리동", "광정동", "궁내동", "재궁동", "오금동"]},
    "uiwong": {"name": "의왕시", "dongs": ["고천동", "부곡동", "오전동", "내손동", "청계동", "초평동", "포일동"]},
    "anseong": {"name": "안성시", "dongs": ["공도읍", "죽산면", "일죽면", "미양면", "대덕면", "양성면", "원곡면", "고삼면", "보개면", "서운면", "금광면", "안성동"]},
    "gapyeong": {"name": "가평군", "dongs": ["가평읍", "설악면", "청평면", "상면", "조종면", "북면"]},
    "yangpyeong": {"name": "양평군", "dongs": ["양평읍", "강상면", "강하면", "옥천면", "서종면", "지평면"]},
    "yeoncheon": {"name": "연천군", "dongs": ["연천읍", "전곡읍", "군남면", "청산면", "미산면", "백학면"]}
}

# 5. 인천광역시 최신 2군 9구 체제 데이터
incheon_regions = {
    "jemulpo": {"name": "제물포구", "dongs": ["중구내륙동", "동구동", "내동", "관동", "북성동", "송월동", "송현동", "화수동", "화평동", "만석동", "송림동"]},
    "yeongjong": {"name": "영종구", "dongs": ["중산동", "운서동", "운남동", "덕교동", "ulwang-dong", "무의동"]},
    "michuhol": {"name": "미추홀구", "dongs": ["도화동", "주안동", "학익동", "관교동", "문학동", "숭의동", "용현동"]},
    "yeonsu": {"name": "연수구", "dongs": ["옥련동", "연수동", "청학동", "동춘동", "송도동"]},
    "namdong": {"name": "남동구", "dongs": ["구월동", "간석동", "만수동", "남촌동", "수산동", "서창동", "논현동", "도림동", "고잔동"]},
    "bupyeong": {"name": "부평구", "dongs": ["부평동", "산곡동", "청천동", "십정동", "일신동", "갈산동", "삼산동", "부개동"]},
    "gyeyang": {"name": "계양구", "dongs": ["효성동", "작전동", "서운동", "계산동", "임학동", "병방동", "방축동", "동양동", "귤현동", "상야동", "하야동"]},
    "seohae": {"name": "서해구", "dongs": ["가좌동", "석남동", "신현동", "원창동", "가정동", "심곡동", "공촌동", "연희동", "당하동", "마전동", "오류동", "왕길동"]},
    "geomdan": {"name": "검단구", "dongs": ["마전동", "당하동", "원당동", "불로동", "대곡동", "금곡동", "오류동", "왕길동", "백석동", "시천동", "검암동", "아라동"]},
    "ganghwa": {"name": "강화군", "dongs": ["강화읍", "선원면", "불은면", "길상면", "화도면", "양도면", "내가면", "하점면", "송해면"]},
    "ongjin": {"name": "옹진군", "dongs": ["북도면", "연평면", "백령면", "대청면", "덕적면", "자월면", "영흥면"]}
}

# 6. 메인 인덱스 페이지 HTML 템플릿
INDEX_HTML_TEMPLATE = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="naver-site-verification" content="{NAVER_VERIFICATION}" />
    <title>오프모드건마사랑 - 서울·경기·인천 프리미엄 힐링·아로마 스웨디시 24시</title>
    <meta name="description" content="서울, 경기, 인천 수도권 전 지역 30분 내 방문. 아로마, 스웨디시, 감성 힐링 전문 관리사가 제공하는 100% 후불제 안심 케어 서비스.">
    <meta name="robots" content="index,follow">
    
    <!-- Open Graph (SNS 미리보기 최적화) -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="오프모드건마사랑 - 서울·경기·인천 프리미엄 힐링·아로마 스웨디시 24시">
    <meta property="og:description" content="서울, 경기, 인천 수도권 전 지역 30분 내 방문. 아로마, 스웨디시, 감성 힐링 전문 관리사가 제공하는 100% 후불제 안심 케어 서비스.">
    <meta property="og:url" content="{DOMAIN}/">
    <meta property="og:site_name" content="오프모드건마사랑">

    <meta name="theme-color" content="#ff6b35">
    <link rel="canonical" href="{DOMAIN}/">
    <link rel="stylesheet" href="./styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{ --primary: #ff6b35; --text-dark: #1f2430; --text-muted: #5b6472; --bg-section: #fff5f0; }}
        html {{ scroll-behavior: smooth; }}
        body {{ font-family: 'Noto Sans KR', sans-serif; color: var(--text-dark); line-height: 1.7; background: var(--bg-section); }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        
        .header {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(20, 20, 35, 0.95); backdrop-filter: blur(10px); border-bottom: 1px solid rgba(255,255,255,0.1); }}
        .header-inner {{ display: flex; align-items: center; justify-content: space-between; height: 70px; max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        .logo-text {{ font-size: 1.25rem; font-weight: 700; color: #fff; text-decoration: none; }}
        .logo-text span {{ color: var(--primary); }}
        .nav {{ display: flex; gap: 24px; align-items: center; }}
        .nav a {{ color: #fff; text-decoration: none; font-size: 0.95rem; }}
        .nav-cta {{ background: var(--primary); padding: 8px 18px; border-radius: 20px; font-weight: 700; font-size: 0.9rem; }}

        .hero {{ padding: 150px 20px 80px; text-align: center; background: linear-gradient(180deg, #15151f 0%, #252030 100%); color: #fff; }}
        .hero h1 {{ font-size: clamp(28px, 5vw, 44px); font-weight: 700; margin-bottom: 16px; line-height: 1.3; }}
        .hero h1 span {{ color: var(--primary); }}
        .hero p {{ font-size: 1.05rem; color: #b5b5c6; margin-bottom: 20px; }}

        .section {{ padding: 80px 0; }}
        .section-white {{ background: #fff; }}
        .section-title {{ text-align: center; margin-bottom: 40px; }}
        .section-title h2 {{ font-size: 1.8rem; margin-bottom: 10px; color: var(--text-dark); }}
        .section-title p {{ color: var(--text-muted); }}

        .partner-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }}
        .card {{ background: #fdfcfb; border: 1px solid #eee; border-radius: 16px; padding: 25px; text-align: left; box-shadow: 0 2px 10px rgba(0,0,0,0.02); transition: transform 0.2s; }}
        .card:hover {{ transform: translateY(-3px); }}
        .card-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }}
        .card h3 {{ font-size: 1.15rem; color: var(--text-dark); font-weight: 700; }}
        .badge {{ background: #fff5f0; color: var(--primary); padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; }}
        .card p {{ color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px; }}
        .card-footer {{ display: flex; justify-content: space-between; align-items: center; }}
        .tel {{ font-weight: bold; color: var(--text-dark); font-size: 0.95rem; }}
        .btn-call {{ background: var(--primary); color: #fff; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-size: 0.85rem; font-weight: bold; }}

        .area-grid {{ display: flex; gap: 15px; justify-content: center; flex-wrap: wrap; }}
        .area-btn {{ background: #fff; border: 1.5px solid var(--primary); color: var(--primary); padding: 12px 28px; border-radius: 30px; text-decoration: none; font-weight: 500; transition: all 0.2s; }}
        .area-btn:hover {{ background: var(--primary); color: #fff; }}

        footer {{ background: #111; color: #888; padding: 40px 20px; text-align: center; font-size: 0.85rem; line-height: 1.6; }}
        footer strong {{ color: #aaa; }}
    </style>
</head>
<body>

    <header class="header">
        <div class="header-inner">
            <a href="/" class="logo-text">오프모드<span>건마사랑</span></a>
            <nav class="nav">
                <a href="#partners">공식제휴샵</a>
                <a href="#regions">지역안내</a>
                <a href="tel:050712803344" class="nav-cta">제휴 문의</a>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <div style="margin-bottom: 30px; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
                <img src="images/banner.jpg" alt="오프모드건마사랑 프리미엄 배너" style="width: 100%; height: auto; display: block; max-height: 400px; object-fit: cover;">
            </div>
            <span style="color: var(--primary); font-size: 0.85rem; letter-spacing: 2px; font-weight: 700; display: inline-block; margin-bottom: 15px;">24H 수도권 프라이빗 힐링 플랫폼</span>
            <h1>일상의 긴장을 끄고(Off),<br>완벽한 휴식을 켜다 <span>오프모드건마사랑</span></h1>
            <p>서울·경기·인천 수도권 전 지역 신속 방문 · 100% 후불제 안심 케어 서비스</p>
        </div>
    </section>

    <section class="section section-white" id="partners">
        <div class="container">
            <div class="section-title">
                <h2>공식 제휴 힐링샵 안내</h2>
                <p>엄선된 전문 관리사의 맞춤형 프리미엄 케어 서비스</p>
            </div>
            <div class="partner-grid">
                <div class="card">
                    <div class="card-header">
                        <h3>퀸즈홈테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>프리미엄 맞춤 홈케어 및 스웨디시 전문 관리 프로그램</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3296</span>
                        <a href="tel:050712803296" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>한국골든테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>정통 힐링 아로마 및 피로 회복 전신 관리 시스템</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3360</span>
                        <a href="tel:050712803360" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>한국미인테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>편안하고 아늑한 환경에서 진행되는 1:1 맞춤 케어</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3201</span>
                        <a href="tel:050712803201" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>오늘밤테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>24시 신속 방문 및 일상 속 깊은 피로 회복 전문</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3199</span>
                        <a href="tel:050712803199" class="btn-call">전화 연결</a>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                        <h3>주주테라피</h3>
                        <span class="badge">제휴점</span>
                    </div>
                    <p>부드러운 감성 힐링과 전문 테라피 복합 코스</p>
                    <div class="card-footer">
                        <span class="tel">📞 0507-1280-3197</span>
                        <a href="tel:050712803197" class="btn-call">전화 연결</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section" id="regions">
        <div class="container">
            <div class="section-title">
                <h2>수도권 서비스 지역</h2>
                <p>서울, 경기, 인천 구/동 단위 실시간 제휴 안내</p>
            </div>
            <div class="area-grid">
                <a href="./seoul/" class="area-btn">서울 전지역</a>
                <a href="./gyeonggi/" class="area-btn">경기 전지역</a>
                <a href="./incheon/" class="area-btn">인천 전지역</a>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p><strong>오프모드건마사랑</strong> | 수도권 힐링 정보 플랫폼</p>
            <p>본 사이트는 제휴 업체의 정보를 안내하는 정보 플랫폼이며 통신판매의 당사자가 아닙니다. 서비스 이용 관련 사항은 각 제휴점에 직접 문의하시기 바랍니다.</p>
            <p style="margin-top: 20px;">&copy; 2026 오프모드건마사랑 All rights reserved.</p>
        </div>
    </footer>

</body>
</html>
"""

# 7. 지역별 페이지 HTML 템플릿 (OG 제목/설명 완벽 포함)
def get_regional_html_template(area_title, path_depth, sub_links=None):
    prefix = "../" * path_depth
    
    sub_links_html = ""
    if sub_links:
        links_box = ""
        for name, url in sub_links.items():
            links_box += f'<a href="{url}" style="background:#fff; border:1px solid #ffd0c2; color:#ff6b35; padding:8px 14px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:500; display:inline-block;">{name}</a> '
        sub_links_html = f"""
        <div style="background:#fff; border-radius:16px; padding:25px; margin-bottom:30px; text-align:left; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <h3 style="font-size:1.1rem; margin-bottom:15px; color:#1f2430;">📂 하위 지역 바로가기</h3>
            <div style="display:flex; flex-wrap:wrap; gap:8px;">
                {links_box}
            </div>
        </div>
        """

    partners_html = ""
    for shop in PARTNER_SHOPS:
        partners_html += f"""
        <div style="background:#fff; border:1px solid #eee; border-radius:12px; padding:20px; text-align:left; box-shadow:0 2px 10px rgba(0,0,0,0.02);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <h3 style="font-size:1.1rem; color:#1f2430; font-weight:700;">{shop['name']}</h3>
                <span style="background:#fff5f0; color:#ff6b35; padding:4px 10px; border-radius:20px; font-size:0.8rem; font-weight:bold;">제휴점</span>
            </div>
            <p style="color:#5b6472; font-size:0.9rem; margin-bottom:15px;">{shop['desc']}</p>
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:bold; color:#1f2430;">📞 {shop['tel']}</span>
                <a href="tel:{shop['tel']}" style="background:#ff6b35; color:#fff; padding:8px 16px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:bold;">전화 연결</a>
            </div>
        </div>
        """

    page_title = f"{area_title} 출장마사지·스웨디시 제휴샵 | 오프모드건마사랑"
    page_desc = f"{area_title} 지역 전문 제휴업체 정보. 30분 내 방문, 아로마 및 스웨디시 100% 후불제 안심 케어."

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="naver-site-verification" content="{NAVER_VERIFICATION}" />
    <title>{page_title}</title>
    <meta name="description" content="{page_desc}">
    <meta name="robots" content="index,follow">
    
    <!-- Open Graph (지역 페이지 미리보기 최적화) -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{page_desc}">
    <meta property="og:url" content="{DOMAIN}">
    <meta property="og:site_name" content="오프모드건마사랑">

    <link rel="canonical" href="{DOMAIN}">
    <link rel="stylesheet" href="{prefix}styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        :root {{ --primary: #ff6b35; --text-dark: #1f2430; --text-muted: #5b6472; --bg-section: #fff5f0; }}
        body {{ font-family: 'Noto Sans KR', sans-serif; color: var(--text-dark); line-height: 1.7; background: var(--bg-section); }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        .header {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(20, 20, 35, 0.95); height: 70px; display: flex; align-items: center; justify-content: space-between; padding: 0 20px; }}
        .logo-text {{ color: #fff; font-weight: 700; text-decoration: none; font-size: 1.2rem; }}
        .logo-text span {{ color: var(--primary); }}
        .main-content {{ padding: 120px 20px 80px; text-align: center; }}
        .partner-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 20px; text-align: left; }}
    </style>
</head>
<body>
    <header class="header">
        <div class="container" style="display:flex; justify-content:space-between; width:100%; align-items:center;">
            <a href="{prefix}index.html" class="logo-text">오프모드<span>건마사랑</span></a>
            <a href="tel:050712803296" style="color:#fff; text-decoration:none; font-weight:700; background:var(--primary); padding:8px 16px; border-radius:20px;">통합 문의</a>
        </div>
    </header>
    <main class="main-content">
        <div class="container">
            <div style="margin-bottom: 30px; border-radius: 16px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.08); max-width: 900px; margin-left: auto; margin-right: auto;">
                <img src="{prefix}images/banner.jpg" alt="{area_title} 프리미엄 제휴 배너" style="width: 100%; height: auto; display: block; max-height: 320px; object-fit: cover;">
            </div>
            <div style="background:#fff; border-radius:16px; padding:30px 20px; max-width:900px; margin:0 auto 30px; box-shadow:0 4px 20px rgba(0,0,0,0.05);">
                <span style="color:var(--primary); font-weight:700; font-size:0.9rem;">수도권 프리미엄 제휴 플랫폼</span>
                <h1 style="font-size:2rem; margin:15px 0 10px;">{area_title} 공식 제휴 힐링샵 안내</h1>
                <p style="color:var(--text-muted); margin-bottom:10px;">{area_title} 전 지역 신속 방문 가능한 엄선된 제휴 업체 리스트입니다.</p>
            </div>
            {sub_links_html}
            <h2 style="font-size:1.4rem; margin-bottom:15px; text-align:left;">📍 {area_title} 실시간 제휴 업체 현황</h2>
            <div class="partner-grid">
                {partners_html}
            </div>
        </div>
    </main>
</body>
</html>
"""

# 8. 전체 빌드 실행 함수
def generate_all_sites():
    print("🚀 [오프모드건마사랑] 수도권 전체 시/도, 구, 동 및 메인 페이지 자동 빌드 시작...")
    
    output_dir = "."
    os.makedirs(output_dir, exist_ok=True)
    
    # 1) 메인 인덱스 페이지 자동 생성
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(INDEX_HTML_TEMPLATE)
    print("✅ 메인 인덱스(index.html) 생성 완료!")

    url_list = [f"{DOMAIN}/"]
    page_count = 1

    all_regions_data = {
        "seoul": {"name": "서울", "districts": seoul_regions},
        "gyeonggi": {"name": "경기", "districts": gyeonggi_regions},
        "incheon": {"name": "인천", "districts": incheon_regions}
    }

    for reg_key, reg_val in all_regions_data.items():
        reg_dir = os.path.join(output_dir, reg_key)
        os.makedirs(reg_dir, exist_ok=True)
        
        dist_links = {}
        for dist_key, dist_val in reg_val["districts"].items():
            dist_links[dist_val["name"]] = f"./{dist_key}/"

        reg_title = f"{reg_val['name']} 전지역"
        with open(os.path.join(reg_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(get_regional_html_template(reg_title, 1, sub_links=dist_links))
        url_list.append(f"{DOMAIN}/{reg_key}/")
        page_count += 1

        for dist_key, dist_val in reg_val["districts"].items():
            dist_dir = os.path.join(reg_dir, dist_key)
            os.makedirs(dist_dir, exist_ok=True)
            
            dong_links = {}
            for dong in dist_val["dongs"]:
                dong_links[dong] = f"./{dong}/"

            dist_title = f"{reg_val['name']} {dist_val['name']}"
            with open(os.path.join(dist_dir, "index.html"), "w", encoding="utf-8") as f:
                f.write(get_regional_html_template(dist_title, 2, sub_links=dong_links))
            url_list.append(f"{DOMAIN}/{reg_key}/{dist_key}/")
            page_count += 1

            for dong in dist_val["dongs"]:
                dong_dir = os.path.join(dist_dir, dong)
                os.makedirs(dong_dir, exist_ok=True)
                
                dong_title = f"{reg_val['name']} {dist_val['name']} {dong}"
                with open(os.path.join(dong_dir, "index.html"), "w", encoding="utf-8") as f:
                    f.write(get_regional_html_template(dong_title, 3))
                url_list.append(f"{DOMAIN}/{reg_key}/{dist_key}/{dong}/")
                page_count += 1

    # sitemap.xml 생성
    sitemap_path = os.path.join(output_dir, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as sm:
        sm.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        sm.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in url_list:
            sm.write(f'  <url>\n    <loc>{u}</loc>\n    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n')
        sm.write('</urlset>')

    print(f"✨ 총 {page_count}개의 SEO 최적화 페이지와 sitemap.xml 생성이 성공적으로 완료되었습니다!")

if __name__ == "__main__":
    generate_all_sites()