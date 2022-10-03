const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

if (urlParams.has('term')){
    if (!isNaN(urlParams.get('term'))){
        const config_src = 'config_t' + urlParams.get('term') + '.js';
        const script = document.createElement('script');
        script.src = config_src;
        document.head.append(script);
        window.onload = update;
    }
}

function isDate(d){
    var date = d.split(' ').length == 2 ? d.split(' ')[1] : d;
    var [month, day, year, ..._] = date.split('/');
    if (!isNaN(month) && !isNaN(day) && !isNaN(year)){
        return true;
    } else {
        return false;
    }
}

function update(){
    // Get all keys from para variable in config file
    var keys = [];
    for (var key in para){
        if(para.hasOwnProperty(key)){
        keys.push(key);
        }
    }
    
    // Add para values by key to all v tags
    keys.forEach(key => {
        var es = [...document.querySelectorAll('v[k="' + key + '"]')];
        if (es.length > 0){
            es.forEach(e => {
                e.innerHTML = para[key];
            });
        }
    });
    
    // Add full day name in front of date
    const weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                      'Thursday', 'Friday', 'Saturday'];
    var es = [... document.querySelectorAll('v.day')];
    if (es.length > 0){
        es.forEach(e => {
            if (isDate(e.innerHTML)){
                const d = new Date(e.innerHTML);
                e.innerHTML = weekdays[d.getDay()] + ' ' + e.innerHTML;
            }
        });
    }
    
    // Add day abbreviation in front of date
    const weekday_abbr = ['Su', 'M', 'T', 'W', 'R', 'F', 'Sa'];
    var es = [... document.querySelectorAll('v.day_abbreviation')];
    if (es.length > 0){
        es.forEach(e => {
            if (isDate(e.innerHTML)){
                const d = new Date(e.innerHTML);
                e.innerHTML = weekday_abbr[d.getDay()] + ' ' + e.innerHTML;
            }
        });
    }
    var es = [... document.querySelectorAll('v.day_abbr')];
    if (es.length > 0){
        es.forEach(e => {
            if (isDate(e.innerHTML)){
                const d = new Date(e.innerHTML);
                e.innerHTML = weekday_abbr[d.getDay()] + ' ' + e.innerHTML;
            }
        });
    }
    
    // Change dates to long do format (month.day.year)
    var es = [... document.querySelectorAll('v.long_dot')];
    if (es.length > 0){
        es.forEach(e => {
            if (isDate(e.innerHTML)){
                e.innerHTML = e.innerHTML.replaceAll('/', '.');
            }
        });
    }
    
    // Change dates to short dot format (month.day)
    var es = [... document.querySelectorAll('v.short_dot')];
    if (es.length > 0){
        es.forEach(e => {
            if (isDate(e.innerHTML)){
                e.innerHTML = e.innerHTML.replaceAll('/', '.').slice(0, -5);
            }
        });
    }
    
    // Change dates to short format (month/day)
    var es = [... document.querySelectorAll('v.short')];
    if (es.length > 0){
        es.forEach(e => {
            if (isDate(e.innerHTML)){
                e.innerHTML = e.innerHTML.slice(0, -5);
            }
        });
    }
}