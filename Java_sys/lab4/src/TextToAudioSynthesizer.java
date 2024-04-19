import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
public class TextToAudioSynthesizer {

    public static void main(String[] args) {
      String text = "Сайн байна уу";
      synthesize(text);
    }
  
    private static void synthesize(String text) {
      String apiUrl = "https://api.chimege.com/v1.2/synthesize";
      String apiToken = "3a05b3a614188441623e778b4475e7f59e0a2f1552314168f51d0d8fb0c3356e";
  
      try {
        URL url = new URL(apiUrl);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "text/plain");
        connection.setRequestProperty("Token", apiToken);
        connection.setDoOutput(true);
  
        try (OutputStream os = connection.getOutputStream()) {
          byte[] input = text.getBytes(StandardCharsets.UTF_8);
          os.write(input, 0, input.length);
        }
  
        int responseCode = connection.getResponseCode();
  
        if (responseCode == HttpURLConnection.HTTP_OK) {
          try (FileOutputStream outputStream = new FileOutputStream("audio.wav")) {
            byte[] buffer = new byte[1024]; // Adjust buffer size as needed
            int bytesRead;
            while ((bytesRead = connection.getInputStream().read(buffer)) != -1) {
              outputStream.write(buffer, 0, bytesRead);
            }
          }
        } else {
          System.out.println("Error: " + responseCode);
        }
  
        connection.disconnect();
      } catch (IOException e) {
        e.printStackTrace();
      }
    }
  }