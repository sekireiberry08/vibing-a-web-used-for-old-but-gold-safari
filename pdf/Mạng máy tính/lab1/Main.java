import java.io.*;
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap domain (vd: www.google.com): ");
        String domain = scanner.nextLine().trim();
        int port = 80;

        try {
            InetAddress addr = InetAddress.getByName(domain);
            System.out.println("Dang ket noi toi IP: " + addr.getHostAddress());
            
            Socket socket = new Socket(addr, port);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            
            BufferedReader in = new BufferedReader(
                new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8)
            );

            out.println("GET / HTTP/1.1");
            out.println("Host: " + domain);
            out.println("User-Agent: Mozilla/5.0");
            out.println("Connection: close");
            out.println();

            String responseLine;
            boolean isHeader = true;
            String fileName = "homepage.html";

            BufferedWriter fileWriter = new BufferedWriter(
                new OutputStreamWriter(new FileOutputStream(fileName), StandardCharsets.UTF_8)
            );

            System.out.println("\n--- DANG TAI DU LIEU ---");

            while ((responseLine = in.readLine()) != null) {
                if (isHeader) {
                    if (responseLine.isEmpty()) {
                        isHeader = false;
                    }
                    continue;
                }

                fileWriter.write(responseLine);
                fileWriter.newLine();
            }

            fileWriter.close();
            in.close();
            socket.close();
            
            System.out.println("\n[THANH CONG] Da download trang chu va luu vao file: " + fileName);

        } catch (UnknownHostException e) {
            System.err.println("Khong tim thay host: " + domain);
        } catch (IOException e) {
            System.err.println("Loi I/O khi ket noi: " + e.getMessage());
        }
    }
}