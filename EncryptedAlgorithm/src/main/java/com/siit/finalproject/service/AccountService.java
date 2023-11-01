package com.siit.finalproject.service;



import com.siit.finalproject.entity.*;

import org.springframework.stereotype.Service;

import java.io.*;
import java.util.*;

@Service
public class AccountService {

    GeneratorMatrixEntity generatorMatrix = new GeneratorMatrixEntity();
    P_Entity pEntity = new P_Entity();
    S_Entity sEntity = new S_Entity();
    PublicKeyEntity publicKey = new PublicKeyEntity();
    EncryptMessageEntity encryptMessage = new EncryptMessageEntity();

    public void addAccount(AccountEntity account) throws IOException {

        String password = account.getPassword();

        createGeneratorMatrix(generatorMatrix,7,10);
        createP_Matrix(pEntity,generatorMatrix);
        createS_Matrix(sEntity,generatorMatrix);
        createPublicKey(generatorMatrix, pEntity, sEntity, publicKey);

        char [] chars = password.toCharArray();
        int [] binaryPassword = new int[chars.length*7];
        int e = 0;
        for (char aChar : chars) {
           String binaryLetter = Integer.toBinaryString(aChar);
           char [] binaryChars = binaryLetter.toCharArray();
            for(int i=0; i<7; i++)
            {
                binaryPassword[e] = binaryChars[i] - '0';
                e++;
            }
        }
//        int [] binaryPassword = new int[] {1,0,1,1};
        printPublicKey();
        int encryptPasswordLength = publicKey.getColumns();
        createEncryptMessage(binaryPassword, encryptPasswordLength, publicKey, encryptMessage);

    }

    private void createEncryptMessage(int[] binaryPassword, int encryptPasswordLength, PublicKeyEntity publicKey, EncryptMessageEntity encryptMessage) throws IOException {

        encryptMessage.setLength(encryptPasswordLength);
        encryptMessage.setEncryptMessage(new int[encryptPasswordLength]);
        int [] aux = new int [encryptPasswordLength];
        System.out.println(" m*G: ");
        for (int j = 0; j < publicKey.getColumns(); j++) {
            int e = 0;
            for (int k = 0; k < publicKey.getRows(); k++) {
                e += binaryPassword[k] * publicKey.getPublicKeyElement(k, j);
            }
            if(e % 2 == 0)
                encryptMessage.setEncryptMessage(j,0);
            else
                encryptMessage.setEncryptMessage(j,1);

            System.out.println(e);
            System.out.println("\n");

        }
        int [] error = createRandomError(encryptPasswordLength,encryptMessage);
        for(int i = 0; i < encryptPasswordLength; i++)
        {
            if((encryptMessage.getEncryptMessageElement(i) + error[i]) % 2 == 0)
                encryptMessage.setEncryptMessage(i,0);
            else
                encryptMessage.setEncryptMessage(i,1);
        }

        printEncryptMessage(encryptPasswordLength,encryptMessage);
    }

    private void printEncryptMessage(int passwordLength, EncryptMessageEntity encryptMessage) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("C:/Users/DODO/Git/EncryptedAlgorithm/src/main/resources/encryptMessage.txt", false));

        for(int i=0;i< passwordLength;i++){
            int g = encryptMessage.getEncryptMessageElement(i);
            if(g==0)
            {
                writer.append('0'+" ");
            }
            else
                writer.append('1'+" ");

            writer.append('\n');
        }
        writer.close();
    }

    private int [] createRandomError(int passwordLength, EncryptMessageEntity encryptMessage) {
        int [] error = new int[passwordLength];
        Random rand = new Random();
        int int_random = rand.nextInt(passwordLength);
        System.out.println("error is : ");
        for(int i=0; i< passwordLength; i++)
        {
            if(i == int_random)
                error[i] = 1;
            else
                error[i] = 0;

            System.out.println(error[i]);
        }
        return error;
    }


    public void printPublicKey() throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("C:/Users/DODO/Git/EncryptedAlgorithm/src/main/resources/publicKey.txt", false));

        for(int i=0;i< publicKey.getRows();i++){
            for(int j=0;j< publicKey.getColumns();j++)
            {
                int g = publicKey.getPublicKeyElement(i,j);
                if(g==0)
                {
                    writer.append('0'+" ");
                }
                else
                    writer.append('1'+" ");
            }

            writer.append('\n');
        }

        writer.close();
    }


    public static void createGeneratorMatrix(GeneratorMatrixEntity generatorMatrix, int rows, int columns) throws IOException {

        BufferedReader file = new BufferedReader(new FileReader("C:/Users/DODO/Git/EncryptedAlgorithm/src/main/resources/generatorMatrix.txt"));
        String line;
        generatorMatrix.setRows(rows);
        generatorMatrix.setColumns(columns);
        generatorMatrix.setGeneratorMatrix(new int[rows][columns]);
        for (int i = 0; i < generatorMatrix.getRows(); i++)
        {
            line = file.readLine();
            String[] values = line.split(" ");
            int e = 0;
            for (int j = 0; j < generatorMatrix.getColumns(); j++) {
                generatorMatrix.setGeneratorMatrix(i,j,Integer.parseInt(values[e]));
                e++;
            }
        }
    }

    public static void createP_Matrix(P_Entity pMatrix, GeneratorMatrixEntity generatorMatrix) throws IOException {

        BufferedReader file = new BufferedReader(new FileReader("C:/Users/DODO/Git/EncryptedAlgorithm/src/main/resources/P.txt"));
        String line;
        int rows = generatorMatrix.getColumns();
        int columns = generatorMatrix.getColumns();
        pMatrix.setRows(rows);
        pMatrix.setColumns(columns);
        pMatrix.setP_Matrix(new int[rows][columns]);
        for (int i = 0; i < pMatrix.getRows(); i++)
        {
            line = file.readLine();
            String[] values = line.split(" ");
            int e = 0;
            for (int j = 0; j < pMatrix.getColumns(); j++) {
                pMatrix.setP_Matrix(i,j,Integer.parseInt(values[e]));
                e++;
            }
        }

    }

    public static void createS_Matrix(S_Entity sMatrix, GeneratorMatrixEntity generatorMatrix) throws IOException {

        BufferedReader file = new BufferedReader(new FileReader("C:/Users/DODO/Git/EncryptedAlgorithm/src/main/resources/S.txt"));
        String line;
        int rows = generatorMatrix.getRows();
        int columns = generatorMatrix.getRows();
        sMatrix.setRows(rows);
        sMatrix.setColumns(columns);
        sMatrix.setS_Matrix(new int[rows][columns]);
        for (int i = 0; i < sMatrix.getRows(); i++)
        {
            line = file.readLine();
            String[] values = line.split(" ");
            int e = 0;
            for (int j = 0; j < sMatrix.getColumns(); j++) {
                sMatrix.setS_Matrix(i,j,Integer.parseInt(values[e]));
                e++;
            }
        }
    }
    private void createPublicKey(GeneratorMatrixEntity generatorMatrix, P_Entity pEntity, S_Entity sEntity, PublicKeyEntity publicKey) {
        int auxMatrix[][] = new int[generatorMatrix.getRows()][generatorMatrix.getColumns()];
        publicKey.setRows(generatorMatrix.getRows());
        publicKey.setColumns(generatorMatrix.getColumns());
        publicKey.setPublicKey(new int[generatorMatrix.getRows()][generatorMatrix.getColumns()]);
        multiplyS_G(generatorMatrix, sEntity, auxMatrix);
        multiplyG_P(generatorMatrix, pEntity, sEntity, publicKey,auxMatrix);

    }

    private static void multiplyG_P(GeneratorMatrixEntity generatorMatrix, P_Entity pEntity, S_Entity sEntity, PublicKeyEntity publicKey, int[][] auxMatrix) {
        for (int i = 0; i < generatorMatrix.getRows(); i++) {
            for (int j = 0; j < pEntity.getColumns(); j++) {
                int e = 0;
                for (int k = 0; k < pEntity.getRows(); k++) {
                    e += auxMatrix[i][k] * pEntity.getP_MatrixElement(k, j);
                }
                if(e % 2 == 0)
                    publicKey.setPublicKey(i,j,0);
                else
                    publicKey.setPublicKey(i,j,1);
            }
        }
    }

    private static void multiplyS_G(GeneratorMatrixEntity generatorMatrix, S_Entity sEntity, int[][] auxMatrix) {
        for (int i = 0; i < sEntity.getRows(); i++) {
            for (int j = 0; j < generatorMatrix.getColumns(); j++) {
                auxMatrix[i][j] = 0;
                int e = 0;
                for (int k = 0; k < generatorMatrix.getRows(); k++) {
                    e += sEntity.getS_MatrixElement(i, k) * generatorMatrix.getGeneratorMatrixElement(k, j);
                }
                if(e % 2 == 0)
                    auxMatrix[i][j] = 0;
                else
                    auxMatrix[i][j] = 1;
            }
        } 
    }
}
