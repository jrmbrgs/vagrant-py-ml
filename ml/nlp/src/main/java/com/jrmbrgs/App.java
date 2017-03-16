package com.jrmbrgs;

import java.io.FileInputStream;
import java.io.InputStream;

import opennlp.tools.namefind.NameFinderME;
import opennlp.tools.namefind.TokenNameFinderModel;
import opennlp.tools.tokenize.Tokenizer;
import opennlp.tools.tokenize.TokenizerME;
import opennlp.tools.tokenize.TokenizerModel;
import opennlp.tools.util.Span;

public class App 
{
    static String sentence = "I want to go to New-york City";

    public static void main(String args[]) throws Exception{
        System.out.println("Try");

        InputStream inputStreamTokenizer = new
            FileInputStream("/ml/en-token.bin");
        TokenizerModel tokenModel = new TokenizerModel(inputStreamTokenizer);

        //String paragraph = "Mike and Smith are classmates";
        String paragraph = "I want to go to New-york City";

        //Instantiating the TokenizerME class
        TokenizerME tokenizer = new TokenizerME(tokenModel);
        String tokens[] = tokenizer.tokenize(paragraph);

        //Loading the NER-location moodel
        InputStream inputStreamNameFinder = new
            FileInputStream("/ml/en-ner-location.bin");
        TokenNameFinderModel model = new TokenNameFinderModel(inputStreamNameFinder);
        //Instantiating the NameFinderME class
        NameFinderME nameFinder = new NameFinderME(model);

        //Finding the names of a location
        Span nameSpans[] = nameFinder.find(tokens);
        //Printing the spans of the locations in the sentence
        for(Span s: nameSpans)
            System.out.println(s.toString()+"  "+tokens[s.getStart()]);
    }
}
