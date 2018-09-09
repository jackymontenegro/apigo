package main

import (
"net/http"
)

func main() {
	url := "https://graph.facebook.com/v3.1/318172115578866/feed?message=UNA%20EMERGENCIA!%20Mi%20casa%20se%20esta%20incendiando%2C%20por%20favor%20ven%20a%20ayudarme.&access_token=EAAeZCqaUt68QBAE0IVzNZAKCnLZAHOSOEMWuZCkZAubLjQOuSWJf6YnKZApybsccfoCB5ZAWj1lERLRP4l8CWk3lWSZCxSPWsQlSktTdOz9CoDZBgCCH3ciPPZAqbNwVfwD1GEWnRnvcMOgmeMm0u697TZBc3pU6wR2Ld53C4uTGbe2CgoLGZApLZCUULHFn5kK7nsEOPiH5NokmNEQZDZD"

	req, _ := http.NewRequest("POST", url, nil)

	http.DefaultClient.Do(req)
}
