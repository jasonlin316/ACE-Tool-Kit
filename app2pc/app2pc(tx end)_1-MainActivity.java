package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.Socket;
import android.app.Activity;
import android.os.Bundle;
import android.util.Log;


public class MainActivity extends AppCompatActivity {


    Socket socket;
    //從手機裡的"我的檔案"選張照片，準備傳到電腦，
    //因不同的手機路徑可能不同，可自行修改。
    //public static final String file_name = "//storage//emulated//0//Download//123.jpg";
    public static final String file_name = "//storage//emulated//0//DCIM//Camera//Daniel.jpg";

    //Button button1=(Button)findViewById(R.id.button);
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Thread test = new Thread(clientSocket);
        test.start();

    }


    Runnable clientSocket = new Runnable() {

        @Override
        public void run() {

            try {
				//wifi ip location
                InetAddress serverAddr = InetAddress.getByName("192.168.10.143");
                Log.e("Socket", "Client: Connecting...");

                try {
					//customize port number
                    socket = new Socket(serverAddr, 1115);
                    OutputStream outputstream = socket.getOutputStream();

                    File myFile = new File(file_name);

                    if (myFile.exists()) {

                        byte[] mybytearray = new byte[(int) myFile.length()];
                        FileInputStream fis = new FileInputStream(myFile);

                        BufferedInputStream bis = new BufferedInputStream(fis,
                                8 * 1024 );
                        bis.read(mybytearray, 0, mybytearray.length);
                        //輸出到電腦
                        outputstream.write(mybytearray, 0, mybytearray.length);
                        outputstream.flush();

                    } else
                        Log.e("Socket", "file doesn't exist!");

                } catch (Exception e) {

                    Log.e("Socket", "Client: Error", e);

                } finally {

                    socket.close();

                }
            } catch (Exception e) {

            }

        }

    };

}

