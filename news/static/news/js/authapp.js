
const langArr = {
	"en":{
		"log": ["log out",'log in'],
		"delete" : "delete your account",
		"menu" : ["date", "sortby", "category", "source"],
		"category" : ["general", "entertainment", "business", "health", "science", "sports","technology"],
		"source" : ['Aeon', 'BBC', 'Bloomberg', 'CNN', 'Forbes', 'Futurism', 'Harvard Business Review',
				'Inc', 'Independent', 'Investopedia', 'Nautilus', 'Quartz',
				'Scientific American', 'Tech Crunch', 'The Spectator', 'The Times' ],
		"domains" : {'Aeon':'aeon.co', 'BBC':'bbc.com', 'Bloomberg':'bloomberg.com', 'CNN':'cnn.com', 'Forbes':'forbes.com', 'Futurism':'futurism.com', 'Harvard Business Review':'hbr.org',
				'Inc':'inc.com', 'Independent':'independent.co.uk', 'Investopedia':'investopedia.com', 'Nautilus':'nautil.us', 'Quartz':'qz.com',
				'Scientific American':'scientificamerican.com', 'Tech Crunch':'techcrunch.com', 'The Spectator':'spectator.co.uk', 'The Times':'thetimes.co.uk' },
		"sortby" : ["relevancy", "popularity", "publishedAt"],
	},
	"ru":{
		"log": ["выйти",'войти'],
		"delete" : "удалить аккаунт",
		"menu" : ["дата",  "сортировка", "категория", "источник"],
		"категория" : ["общее", "развлечение", "бизнесс", "здоровье", "наука", "спорт", "технология"],
		"источник" : ['BBC News', 'Colta.ru', 'Deutsche Welle', 'Habr', 'Lenta.ru', 'Meduza', 'N+1',
				'Sports.ru', 'Аргументы и факты', 'Ведомости', 'Газета.ру',  'Дождь', 'Известия',
				'Коммерсантъ',  'Радио Свобода',  'РБК', 'РИА Новости',  'Сноб' ],
		"domains" : { 'BBC News':'bbc.com', 'Colta.ru':'colta.ru', 'Deutsche Welle':'dw.com', 'Habr':'habr.com', 'Lenta.ru':'lenta.ru', 'Meduza':'meduza.io', 'N+1':'nplus1.ru',
				'Sports.ru':'sports.ru', 'Аргументы и факты':'aif.ru', 'Ведомости':'vedomosti.ru', 'Газета.ру':'gazeta.ru',  'Дождь': "tvrain.ru", 'Известия':'iz.ru',
				'Коммерсантъ': 'kommersant.ru',  'Радио Свобода':'svoboda.org',  'РБК':'www.rbc.ru', 'РИА Новости':'ria.ru',  'Сноб':'snob.ru'  },
		"сортировка" : ["релеватность", "популярность", "публикация"],
	}
}

window.onload = function loadContIcons() {
let hash = window.location.hash;
hash = hash.substr(1);
if(!(hash.localeCompare('en')==0) && !(hash.localeCompare('ru')==0)){
	location.href = window.location.pathname + '#' + 'ru';
	location.reload();
}
}

function checkFluency(a){
if(a.children[0].checked==true){
	a.children[0].checked = false;
}
else{
	a.children[0].checked = true;
}
}

function changenews(){
let hash = window.location.hash;
hash = hash.substr(1);
path = "?lan=" + hash+"&";
date = document.getElementById("date-news").value;
console.log(hash);
	for (var j = 1; j < langArr[hash]['menu'].length-1; j++) {
		var temp = document.getElementById(langArr['en']['menu'][j]);
		path += langArr['en']['menu'][j] + "=";
		for (var i = 0; i < langArr[hash][langArr[hash]['menu'][j]].length; i++) {
			if (temp.children[i].children[0].children[0].checked == true)
			    path += langArr['en'][langArr['en']['menu'][j]][i] + ",";
		}
//		if (temp.children[i].children[0].children[0].checked == true)
		    path += langArr['en'][langArr['en']['menu'][j]][i] + "&";
	}

	path += "source=";
	var temp = document.getElementById(langArr['en']['menu'][3]);
	for (var i = 0; i < langArr[hash][langArr[hash]['menu'][3]].length; i++) {
		if (temp.children[i].children[0].children[0].checked == true)
		path += langArr[hash]['domains'][langArr[hash][langArr[hash]['menu'][3]][i]] + ",";
	}
//    if (temp.children[i].children[0].children[0].checked == true)
		path += langArr[hash]['domains'][langArr[hash][langArr[hash]['menu'][3]][i]];
	path += '&date=' + date;

location.href = window.location.pathname + path+'#' + hash;
//location.reload();
}

function changeLang(){

console.log(window.location.pathname);
var contentmenu = document.getElementById("menu");
if (contentmenu.children[0].children[0].innerText.localeCompare('en')==0){
		location.href = window.location.pathname + '#' + 'en';
}
else{
		location.href = window.location.pathname + '#' + 'ru';
}

let hash = window.location.hash;
hash = hash.substr(1);
console.log(hash);
path = "?lan="+hash;
location.href = window.location.pathname + path+'#'+ hash;

console.log(window.location.pathname);
//location.reload();

 };


function check_catal(){
var category = document.getElementById("show-category")
var source = document.getElementById("show-source")
if(category.checked){
source.labels[0].style.background="grey"
category.labels[0].style.background="#14181f"
var category_child = document.getElementById("source")
for(var i=0; i<category_child.childElementCount; i++){
category_child.children[i].children[0].children[0].checked=false
}
}
else{
category.labels[0].style.background="grey"
source.labels[0].style.background="#14181f"
var category_child = document.getElementById("category")
for(var i=0; i<category_child.childElementCount; i++){
category_child.children[i].children[0].children[0].checked=false
}
}
}