var exampleModal = document.getElementById('exampleModal')
exampleModal.addEventListener('show.bs.modal', function (event) {
  // Botón que activó el modal
  var button = event.relatedTarget
  // Extraer información de los atributos data-bs-*
  var recipient = button.getAttribute('data-bs-whatever')
  // Si es necesario, puedes iniciar una solicitud AJAX aquí
  // y luego realiza la actualización en una devolución de llamada.
  //
  // Actualizar el contenido del modal.
  var modalTitle = exampleModal.querySelector('.modal-title')
  var modalBodyInput = exampleModal.querySelector('.modal-body input')

  modalTitle.textContent = 'Transportes ' + recipient
  modalBodyInput.value = recipient
})
var exampleModa2 = document.getElementById('exampleModa2')
exampleModa2.addEventListener('show.bs.modal', function (event) {
  // Botón que activó el modal
  var button = event.relatedTarget
  // Extraer información de los atributos data-bs-*
  var recipient = button.getAttribute('data-bs-whatever')
  // Si es necesario, puedes iniciar una solicitud AJAX aquí
  // y luego realiza la actualización en una devolución de llamada.
  //
  // Actualizar el contenido del modal.
  var modalTitle = exampleModa2.querySelector('.modal-title')
  var modalBodyInput = exampleModa2.querySelector('.modal-body input')

  modalTitle.textContent = 'Hospedajes ' + recipient
  modalBodyInput.value = recipient
})
var exampleModa3 = document.getElementById('exampleModa3')
exampleModa3.addEventListener('show.bs.modal', function (event) {
  // Botón que activó el modal
  var button = event.relatedTarget
  // Extraer información de los atributos data-bs-*
  var recipient = button.getAttribute('data-bs-whatever')
  // Si es necesario, puedes iniciar una solicitud AJAX aquí
  // y luego realiza la actualización en una devolución de llamada.
  //
  // Actualizar el contenido del modal.
  var modalTitle = exampleModa3.querySelector('.modal-title')
  var modalBodyInput = exampleModa3.querySelector('.modal-body input')

  modalTitle.textContent = 'Tours ' + recipient
  modalBodyInput.value = recipient
})
var exampleModa4 = document.getElementById('exampleModa4')
exampleModa4.addEventListener('show.bs.modal', function (event) {
  // Botón que activó el modal
  var button = event.relatedTarget
  // Extraer información de los atributos data-bs-*
  var recipient = button.getAttribute('data-bs-whatever')
  // Si es necesario, puedes iniciar una solicitud AJAX aquí
  // y luego realiza la actualización en una devolución de llamada.
  //
  // Actualizar el contenido del modal.
  var modalTitle = exampleModa4.querySelector('.modal-title')
  var modalBodyInput = exampleModa4.querySelector('.modal-body input')

  modalTitle.textContent = 'Tour Aereo ' + recipient
  modalBodyInput.value = recipient
})
var exampleModa5 = document.getElementById('exampleModa5')
exampleModa5.addEventListener('show.bs.modal', function (event) {
  // Botón que activó el modal
  var button = event.relatedTarget
  // Extraer información de los atributos data-bs-*
  var recipient = button.getAttribute('data-bs-whatever')
  // Si es necesario, puedes iniciar una solicitud AJAX aquí
  // y luego realiza la actualización en una devolución de llamada.
  //
  // Actualizar el contenido del modal.
  var modalTitle = exampleModa5.querySelector('.modal-title')
  var modalBodyInput = exampleModa5.querySelector('.modal-body input')

  modalTitle.textContent = 'Canopy Malpais ' + recipient
  modalBodyInput.value = recipient
})
var exampleModa6 = document.getElementById('exampleModa6')
exampleModa6.addEventListener('show.bs.modal', function (event) {
  // Botón que activó el modal
  var button = event.relatedTarget
  // Extraer información de los atributos data-bs-*
  var recipient = button.getAttribute('data-bs-whatever')
  // Si es necesario, puedes iniciar una solicitud AJAX aquí
  // y luego realiza la actualización en una devolución de llamada.
  //
  // Actualizar el contenido del modal.
  var modalTitle = exampleModa6.querySelector('.modal-title')
  var modalBodyInput = exampleModa6.querySelector('.modal-body input')

  modalTitle.textContent = 'Tour Tortuga' + recipient
  modalBodyInput.value = recipient
})