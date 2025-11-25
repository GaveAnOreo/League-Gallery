package JAVAPROJECT;
import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;

public class GradeCalculator {

    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in).useLocale(Locale.US)) {
            DecimalFormat decform = new DecimalFormat("00.00");

            double midtermQuiz1, midtermQuiz2, midtermActivity1, midtermActivity2, midtermAttendance;
        double midtermPerformance;
        double midtermExam;
        double midtermGrade;

        double finalsQuiz1, finalsQuiz2, finalsActivity1, finalsActivity2, finalsAttendance;
        double finalsPerformance;
        double finalsExam;
        double finalsGrade;

        double firstSemGrade;

        System.out.println("--- Enter Midterm Scores ---");
        System.out.print("Enter Quiz 1 score: ");
        midtermQuiz1 = input.nextDouble();
        System.out.print("Enter Quiz 2 score: ");
        midtermQuiz2 = input.nextDouble();
        System.out.print("Enter Activity 1 score: ");
        midtermActivity1 = input.nextDouble();
        System.out.print("Enter Activity 2 score: ");
        midtermActivity2 = input.nextDouble();
        System.out.print("Enter Attendance score: ");
        midtermAttendance = input.nextDouble();

        midtermPerformance = (midtermQuiz1 + midtermQuiz2 + midtermActivity1 + midtermActivity2 + midtermAttendance) / 5.0;
        System.out.println(">>> Calculated Midterm Performance: " + decform.format(midtermPerformance));

        System.out.print("Enter Midterm Exam score: ");
        midtermExam = input.nextDouble();

        midtermGrade = (midtermPerformance * 0.70) + (midtermExam * 0.30);
        System.out.println(">>> Calculated Midterm Grade: " + decform.format(midtermGrade));

        System.out.println("\n------------------------------\n");

        System.out.println("--- Enter Finals Scores ---");
        System.out.print("Enter Quiz 1 score: ");
        finalsQuiz1 = input.nextDouble();
        System.out.print("Enter Quiz 2 score: ");
        finalsQuiz2 = input.nextDouble();
        System.out.print("Enter Activity 1 score: ");
        finalsActivity1 = input.nextDouble();
        System.out.print("Enter Activity 2 score: ");
        finalsActivity2 = input.nextDouble();
        System.out.print("Enter Attendance score: ");
        finalsAttendance = input.nextDouble();

        finalsPerformance = (finalsQuiz1 + finalsQuiz2 + finalsActivity1 + finalsActivity2 + finalsAttendance) / 5.0;
        System.out.println(">>> Calculated Finals Performance: " + decform.format(finalsPerformance));

        System.out.print("Enter Finals Exam score: ");
        finalsExam = input.nextDouble();

        finalsGrade = (finalsPerformance * 0.70) + (finalsExam * 0.30);
        System.out.println(">>> Calculated Finals Grade: " + decform.format(finalsGrade));

        firstSemGrade = (midtermGrade + finalsGrade) / 2.0;

        System.out.println();
        System.out.println("the 1st Sem Grade is:     " + decform.format(firstSemGrade));

        }
    }
}