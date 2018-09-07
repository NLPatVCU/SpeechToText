package nlp.speechToText;

import java.io.InputStream;
import java.util.Scanner;
import java.io.File;
import java.io.FileInputStream;

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
public class TranscriptionAdapt {

    public static void main(String[] args) throws Exception {
	Scanner in = new Scanner(System.in);
	System.out.println("Enter filename");
	File file = new File(in.next());
        in.nextLine();
        System.out.println("Enter transcription");
        String[] ref = in.nextLine().split(" ");
        System.out.println("Loading models...");

        Configuration configuration = new Configuration();

        // Load model from the jar
        // configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");

        // You can also load model from folder
        configuration.setAcousticModelPath("file:./model-training/en-us-adapt");

        configuration
                .setDictionaryPath("file:./model-training/cmudict-en-us.dict");
        configuration
                .setLanguageModelPath("file:./model-training/en-us.lm.bin");

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
	System.out.println("Hypothesis: " + transcription); 
        WordSequenceAligner werEval = new WordSequenceAligner();
        String [] hyp = transcription.split(" ");
        
        System.out.println(werEval.align(ref, hyp));
    }
}
