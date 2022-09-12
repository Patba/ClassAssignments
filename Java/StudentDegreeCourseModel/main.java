import java.util.ArrayList;

class Course{
    public ArrayList<Student> students = new ArrayList<>();

    public ArrayList<Student> getStudents() {
        return students;
    }

    public void setStudents(Student student) {
        students.add(student);
    }

    @Override
    public String toString() {
        return "Course{" +
                "students=" + students +
                '}';
    }
}

class Degree{
    public ArrayList<Course> courses = new ArrayList<>();

    public ArrayList getCourses() {
        return courses;
    }

    public void setCourses(Course course) {
        courses.add(course);
    }

    ArrayList betterStudents(){
        ArrayList betterStudents = new ArrayList<>();
        float avgsum = 0;
        int countstudent = 0;
        for(Course course : this.courses){ //Dla Kursu[1] w Kursach
            for(Student student : course.students){ // Dla Studenta w Studentach w Kursie[1]
                countstudent += 1;
                avgsum += student.getMark();
            }
        }
        avgsum = avgsum / countstudent;
        for(Course course : this.courses){
            for(Student student : course.students){
                if(student.getMark() >= avgsum)
                betterStudents.add(student.getStudent_name());
            }
        }

    return betterStudents;
    }
}
class Student {
    private final int course_mark;
    private final String student_name;

    public Student(String student_name, int course_mark) {
        this.student_name = student_name;
        this.course_mark = course_mark;
    }

    public String getStudent_name() {
        return student_name;
    }

    public int getMark() {
        return course_mark;
    }

}


public class main {
    public static void main(String[] args) {
        Student marek = new Student("Marek", 5);
        Student miroslaw = new Student("Miroslaw", 3);
        Student ania = new Student("Ania", 4);
        Student zbigniew = new Student("Zbigniew", 2);
        Course abba = new Course();
        abba.setStudents(marek);
        abba.setStudents(miroslaw);
        abba.setStudents(ania);
        abba.setStudents(zbigniew);
        Degree informatyka = new Degree();
        informatyka.setCourses(abba);
        System.out.println(informatyka.betterStudents());


    }
}
