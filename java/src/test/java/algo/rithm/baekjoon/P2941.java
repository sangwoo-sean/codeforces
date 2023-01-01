package algo.rithm.baekjoon;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.*;
import java.util.*;

public class P2941 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        int answer = new Solver().solve(str);

        System.out.println(answer);
    }

    @Test
    void test() {
        Assertions.assertEquals(6, new Solver().solve("ljes=njak"));
        Assertions.assertEquals(3, new Solver().solve("ddz=z="));
        Assertions.assertEquals(3, new Solver().solve("nljj"));
        Assertions.assertEquals(2, new Solver().solve("c=c="));
        Assertions.assertEquals(3, new Solver().solve("dz=ak"));
    }
}

class Solver {

    private int count;

    private final List<String> CROATIAN2 = Arrays.asList("c=", "c-", "d-", "lj", "nj", "s=", "z=");
    private final List<String> CROATIAN3 = Arrays.asList("dz=");

    public int solve(String str) {

        for (int i = 0; i < str.length(); ) {
            if (i + 2 < str.length() && isCroatian3(str.substring(i, i + 3))) {
                count++;
                i += 3;
                continue;
            }

            if (i + 1 < str.length() && isCroatian2(str.substring(i, i + 2))) {
                count++;
                i += 2;
                continue;
            }

            count++;
            i++;
        }
        return count;
    }

    private boolean isCroatian2(String tmp) {
        return CROATIAN2.contains(tmp);
    }
    private boolean isCroatian3(String tmp) {
        return CROATIAN3.contains(tmp);
    }
}