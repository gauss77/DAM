package dam2.repoqueries.app.servicio;

import java.util.List;
import java.util.Optional;
import java.util.Set;

import org.springframework.boot.autoconfigure.data.web.SpringDataWebProperties.Sort;
import org.springframework.stereotype.Service;

import dam2.repoqueries.app.modelo.Empleado;

@Service
public interface EmpleadoServicio {
	Set<Empleado>		findAll();
	
	Optional<Empleado>	buscarPorClave(Integer id);
	Optional<Empleado>	insertar(Empleado empleado);
	Optional<Empleado>	actualizar(Empleado empleado);
	boolean				borrarPorClave(Integer id);
	boolean 			existePorClave(Integer id);
	
	Set<Empleado> buscarPorCargo(String cargo);
}
