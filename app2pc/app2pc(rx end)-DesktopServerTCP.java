package java_test;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class DesktopServerTCP implements Runnable {

 public static final int SERVERPORT = 1115;

 // 最後要儲存照片的位置
 public static final String file_name = "C:\\Users\\changda\\Desktop\\12345.jpg";

 public void run() {

  try {

   System.out.println("Server: Connecting...");
   ServerSocket serverSocket = new ServerSocket(SERVERPORT);

   while (true) {

    Socket client = serverSocket.accept();
    System.out.println("Server: Receiving...");

    OutputStream out = new FileOutputStream(file_name);
    byte buf[] = new byte[1024];
    int len;

    // 讀入從手機端傳來的照片
    InputStream inputStream = client.getInputStream();
    try {
     while ((len = inputStream.read(buf)) != -1) {
      // 將照片寫入到電腦裡
      out.write(buf, 0, len);
     }
     out.close();
     inputStream.close();

    } catch (IOException e) {
     e.printStackTrace();
    } finally {

     client.close();
     System.out.println("Server: Done.");

    }

   }

  } catch (Exception e) {

   System.out.println("Server: Error");
   e.printStackTrace();

  }

 }

 public static void main(String str[]) {

  Thread desktopSerThread = new Thread(new DesktopServerTCP());
  desktopSerThread.start();

 }
}