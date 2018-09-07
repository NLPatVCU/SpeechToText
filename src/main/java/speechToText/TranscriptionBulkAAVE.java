package nlp.speechToText;

import java.io.InputStream;
import java.io.File;
import java.io.FileInputStream;
import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.FileWriter;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.api.StreamSpeechRecognizer;
import edu.cmu.sphinx.decoder.adaptation.Stats;
import edu.cmu.sphinx.decoder.adaptation.Transform;
import edu.cmu.sphinx.result.WordResult;
import WER.*;

/**
 * A simple example that shows how to transcribe a continuous audio file that
 * has multiple utterances in it.
 */
public class TranscriptionBulkAAVE {

    public static void main(String[] args) throws Exception {
        Scanner fileScanner = new Scanner(new File("./model-training-all-aave/test_0.txt"));  
        int numberOfFiles = 0;
        double totalWERUnadapted = 0.0;
        double totalWERAdapted = 0.0; 
        while(fileScanner.hasNextLine()) {
            String line = fileScanner.nextLine();
            String[] ref = parseTag(line).split(" ");
            File audioFile = new File(parseFilename(line));
            System.out.println(parseFilename(line));
            numberOfFiles++;
            totalWERUnadapted += runUnadapted(audioFile, ref);
            totalWERAdapted += runAdapt(audioFile, ref);
        }    
        double averageWERAdapted = totalWERAdapted / numberOfFiles;
        double averageWERUnadapted = totalWERUnadapted / numberOfFiles;
        try {
            // Open given file in append mode.
            BufferedWriter out1 = new BufferedWriter(
                   new FileWriter("test_results_unadapted_0.txt", true));
            out1.write("\nadapted with aave vs unadapted with sen"+averageWERUnadapted);
            out1.close();
            BufferedWriter out2 = new BufferedWriter(
                   new FileWriter("test_results_adapted_0.txt", true));
            out2.write("\nadapted with aave vs unadapted with sen"+averageWERAdapted);
            out2.close();
        }
        catch (Exception e) {
            System.out.println("exception occurred" + e);
        }
    }

    public static String parseFilename(String line) {
        return "./model-training-all-aave/" + line.substring(line.indexOf("(") + 1, line.indexOf(")")) + ".wav";
    }

    public static String parseTag(String line) {
        return "./model-training-all-aave/" + line.substring(line.indexOf(">") + 1, line.indexOf("</")).trim();
    }

    public static double runUnadapted(File file, String[] ref) throws Exception {
        Configuration configuration = new Configuration();

        // Load model from the jar
        // configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");

        // You can also load model from folder
        configuration.setAcousticModelPath("file:./model-training-all-aave/en-us");

        configuration
                .setDictionaryPath("file:./model-training-all-aave/cmudict-en-us.dict");
        configuration
                .setLanguageModelPath("file:./model-training-all-aave/en-us.lm.bin");

        StreamSpeechRecognizer recognizer = new StreamSpeechRecognizer(
                configuration);
        InputStream stream = new FileInputStream(file);
        // stream.skip(44);

        // Simple recognition with generic model
        recognizer.startRecognition(stream);
        SpeechResult result;
	    String transcription = "";
        while ((result = recognizer.getResult()) != null) {
	    transcription += result.getHypothesis() + " ";
        }
        recognizer.stopRecognition();
        WordSequenceAligner wer = new WordSequenceAligner();
        String [] hyp = transcription.split(" ");
        return wer.getWER(ref, hyp);
    }

    public static double runAdapt(File file, String[] ref) throws Exception {
        Configuration configuration = new Configuration();

        // Load model from the jar
        // configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");

        // You can also load model from folder
        configuration.setAcousticModelPath("file:./model-training-all-aave/en-us-adapt");

        configuration
                .setDictionaryPath("file:./model-training-all-aave/cmudict-en-us-aave.dict");
        configuration
                .setLanguageModelPath("file:./model-training-all-aave/en-us.lm.bin");

        StreamSpeechRecognizer recognizer = new StreamSpeechRecognizer(
                configuration);
        InputStream stream = new FileInputStream(file);
        // stream.skip(44);

        // Simple recognition with generic model
        recognizer.startRecognition(stream);
        SpeechResult result;
	    String transcription = "";
        while ((result = recognizer.getResult()) != null) {
	    transcription += result.getHypothesis() + " ";
        }
        recognizer.stopRecognition();
        WordSequenceAligner wer = new WordSequenceAligner();
        String [] hyp = transcription.split(" ");
        return wer.getWER(ref, hyp);
    }
}
