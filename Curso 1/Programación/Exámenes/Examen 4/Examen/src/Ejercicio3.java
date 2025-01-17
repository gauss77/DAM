import ejer3.*;

public class Ejercicio3 {
    public static void main(String[] args)  {
        final String USER = GestionEmpleados.requestValue("Enter database user name");
        final String PASSWORD = GestionEmpleados.requestValue("Enter database user password");
        final String DB_NAME = "exProg3Ev";
        DatabaseConnection dbc;
        GestionEmpleados gestorGui;

        try {
            dbc = new DatabaseConnection(DB_NAME, USER, PASSWORD);
            gestorGui = new GestionEmpleados("Gestión de Empleados", 640, 480, dbc);
            gestorGui.enableEvents();
            gestorGui.render();
        }
        catch (RuntimeException excp) {
            System.out.println(excp.getMessage());
        }
    }
}