import java.io.*;
import java.util.Locale;
import java.util.StringTokenizer;

/**
 * TwoSatTest -  client program to test satisfiability of TwoSat
 */

public class TwoSatTest {
    private final InputReader reader;
    private final OutputWriter writer;

    public TwoSatTest(InputReader reader, OutputWriter writer) {
        this.reader = reader;
        this.writer = writer;
    }

    public static void main(String[] args) {
        InputReader reader = new InputReader(System.in);
        OutputWriter writer = new OutputWriter(System.out);
        new TwoSatTest(reader, writer).run();
        writer.writer.flush();
    }


    public void run() {

        int n = reader.nextInt();
        int m = reader.nextInt();
        Clause[] clauses = new Clause[m];
        for (int i = 0; i < m; ++i) {
            clauses[i] = new Clause();
            clauses[i].firstVar = reader.nextInt();
            clauses[i].secondVar = reader.nextInt();
        }

        TwoSat twoSat = new TwoSat(n, clauses);
        twoSat.printAsssignments();
    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public double nextDouble() {
            return Double.parseDouble(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }
    }

    static class OutputWriter {
        public PrintWriter writer;

        OutputWriter(OutputStream stream) {
            writer = new PrintWriter(stream);
        }

        public void printf(String format, Object... args) {
            writer.print(String.format(Locale.ENGLISH, format, args));
        }
    }
}

class Clause {
    int firstVar;
    int secondVar;
}