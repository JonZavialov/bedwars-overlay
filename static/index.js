const hypixelApiKey = "76271442-3196-44cd-bc9d-a7f8708cc597"

function replaceStats(){
    setTimeout(getData, 1000)
}

function getData(){
    console.log('getting data...')
    fetch("/data")
    .then(res => res.json())
    .then(async(out) => {
        let dict = document.getElementById("dict")
        if(dict.innerHTML != out){
            let element = document.getElementById("stats")
            element.innerHTML = ""
            console.log("previous data does not match new data")
            await createStatsString(out)
        }
    })
    replaceStats()
}

function createStatsString(out){
    console.log('creating stats string...')
    let element = document.getElementById("dict")
    element.innerHTML = out
    let stats1 = document.getElementById("stats")
    stats1.innerHTML += "<tr><th>Player</th><th>Stars</th><th>FKDR</th><th>WLR</th><th>Winstreak</th><th>Games Played</th></tr>"
    let playerStats
    for(let i = 0; i < out.length; i++){
        if(out[i] != "PanasonicTV" && out[i] != "b3ttyblxxd" && out[i] != "zyvabxbe"){fetch(`https://api.hypixel.net/player?key=${hypixelApiKey}&name=${out[i]}`)
        .then(res => res.json())
        .then(out => {
            console.log("getting stats for " + out.player.displayname)
            if(out.success == false){
                console.log('error occured')
            }
            let dataList = {
                'stars': out['player']['achievements']['bedwars_level'],
                'final_kdr': out['player']['stats']['Bedwars']['final_kills_bedwars'] / out['player']['stats']['Bedwars']['final_deaths_bedwars'],
                'games_played': out['player']['stats']['Bedwars']['games_played_bedwars'],
                'winstreak': out['player']['stats']['Bedwars']['winstreak'],
                'win_lose_ratio': out['player']['stats']['Bedwars']['wins_bedwars'] / out['player']['stats']['Bedwars']["losses_bedwars"]
            }
            playerStats = `<tr><td>${out.player.displayname}</td> <td>${dataList.stars}</td> <td>${Math.round(100*dataList['final_kdr'])/100}</td> <td>${Math.round(100*dataList["win_lose_ratio"])/100}</td> <td>${dataList.winstreak}</td> <td>${dataList["games_played"]}</td></tr>`
            let element = document.getElementById("stats")
            element.innerHTML += playerStats
        })
        .catch(err => {
            console.log("error")
            statsString = "error!"
        })}
    }
}