package sample;

import javax.swing.*;
import java.awt.*;
import java.awt.geom.AffineTransform;
import java.util.ArrayList;
import java.util.Collections;


public class Main {

    public static class Szachownica extends JComponent {

        public void paint(Graphics g) {
            Graphics2D g2d = (Graphics2D) g;
            g2d.setColor(Color.BLACK);
            g2d.setStroke(new BasicStroke(3));
            g2d.drawRect(30, 30, 400, 400);
            g2d.fillRect(67, 67, 326, 326);

            Graphics2D sRB = (Graphics2D) g;
            Graphics2D sRW = (Graphics2D) g;

            Graphics2D n = (Graphics2D) g;
            Graphics2D t = (Graphics2D) g;
            sRW.setStroke(new BasicStroke(1));
            sRB.setStroke(new BasicStroke(1));
            sRW.setColor(Color.RED);
            sRB.setColor(Color.white);

            int w;
            int h = 70;

            boolean flag = true;

            //Szachownica
            // 1 For do zmiany kolumn, sekwencja ustala poczatek wiersza
            for (int i = 0; i < 8; i++) {
                if (i % 2 == 0) {
                    w = 70;
                } else {
                    w = 110;
                }
                // 2 For do drukowania wiersza, gdy j jest parzysty drukujemy bialy kwadrat
                for (int j = 0; j < 8; j++) {
                    switch (j % 2) {
                        case 0: {
                            sRW.fillRect(w, h, 40, 40);
                            break;
                        }
                        default: {
                            break;
                        }
                    }
                    w += 40;
                }
                // 2
                h += 40; // 3 przesuniecie w dol po utworzeniu calego wiersza
            }
            // 1

            String[] letters = new String[]{"A", "B", "C", "D", "E","F","G","H"};
            sRW.setColor(Color.BLACK);

            Font font = new Font(null, Font.PLAIN, 30);
            t.setFont(font);

            w = 80;
            h = 420;

            for(int i = 0; i<8;i++)
            {
                t.drawString(letters[i],w,h);
                w += 40;
            }

            AffineTransform affineTransform = new AffineTransform();
            affineTransform.rotate((Math.PI / 2) * 2, 0, 0);
            Font rotatedFont = font.deriveFont(affineTransform);
            t.setFont(rotatedFont);

            w = 100;
            h = 40;
            for(int i = 0; i<8;i++)
            {
                t.drawString(letters[i],w,h);
                w += 40;
            }


            String[] numbers = new String[]{"1", "2", "3", "4", "5","6","7","8"};
            n.setFont(font);
            w = 40;
            h = 100;
            affineTransform.rotate((Math.PI / 2) * 2, 0, 0);
            rotatedFont = font.deriveFont(affineTransform);
            n.setFont(rotatedFont);

            for(int i = 7; i>=0;i--)
            {
                n.drawString(numbers[i],w,h);
                h+=40;
            }
            w +=380;
            h = 80;
            affineTransform.rotate((Math.PI / 2)*2, 0, 0);
            rotatedFont = font.deriveFont(affineTransform);
            n.setFont(rotatedFont);
            for(int i = 7; i>=0;i--)
            {
                n.drawString(numbers[i],w,h);
                h+=40;
            }

        }
    }




    public static void main(String[] args) {
        int w = 600;
        int h = 600;
        JFrame jf = new JFrame();
        jf.setSize(w, h);
        jf.setLocationRelativeTo(null);
        jf.setTitle("amogus");
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.getContentPane().setBackground(Color.WHITE);




        Szachownica szachownica = new Szachownica();
        jf.add(szachownica);
        jf.setVisible(true);

    }
}

