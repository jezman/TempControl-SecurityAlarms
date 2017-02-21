package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"time"

	"gopkg.in/telegram-bot-api.v4"
)

var t = time.Now()

func moves() {
	date := t.Format("02-01-2006")
	oldPath := "/oldpath/"
	newPath := "/newpath/" + date + "/"

	fmt.Println(newPath)

	if _, err := os.Stat(newPath); os.IsNotExist(err) {
		os.Mkdir(newPath, 0766)
	}

	files, err := ioutil.ReadDir(oldPath)
	if err != nil {
		log.Fatal(err)
	}
	for _, file := range files {
		if !file.IsDir() {
			err := os.Rename(oldPath+file.Name(), newPath+file.Name())
			if err != nil {
				panic(err)
			}
			fmt.Println(file.Name())
		}
	}
}

func checks() bool {
	hour := t.Hour()
	weekday := t.Weekday()
	if hour <= 8 && hour >= 19 || weekday == time.Sunday || weekday == time.Saturday {
		return true
	}
	return false
}

func main() {
	bot, err := tgbotapi.NewBotAPI("247646851:AAH4GQny2X_iMhvbbdYYFRUFc5AslBkEfkc")
	if err != nil {
		log.Panic(err)
	}

	photo := tgbotapi.NewPhotoUpload(2057901, os.Args[1])
	if checks() {
		bot.Send(photo)
	} else {
		fmt.Println("range is out")
	}

	moves()
}

// def sensor():
//     fl = open('path_to_rid')
//     motion = fl.read()
//     if '1' in motion:
//         return True
