
Split a file into sections by number of seconds
`ffmpeg -i Patient384-R37.wav -f segment -segment_time 30 -c copy out%03d.wav`

Compile
`mvn compile`

Run specific file
`mvn exec:java -Dexec.mainClass=nlp.speechToText.TranscriptionAdapt`
`mvn exec:java -Dexec.mainClass=nlp.speechToText.TranscriptionAdapt -Dexec.args="'argument separated with space' 'another one'"`

If you get an error where it says Audacity is already running:wq
go to ~/Library/Application Support/audacity and trash the contents of the "SessionData" folder plit a file into sections by number of seconds
ffmpeg -i Patient384-R37.wav -f segment -segment_time 30 -c copy out%03d.wav

Run specific file
mvn exec:java -Dexec.mainClass=nlp.speechToText.TranscriptionAdapt
mvn exec:java -Dexec.mainClass=nlp.speechToText.TranscriptionAdapt -Dexec.args="'argument separated with space' 'another one'"

go to ~/Library/Application Support/audacity and trash the contents of the "SessionData" folder 
