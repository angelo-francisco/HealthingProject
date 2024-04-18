from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from medicine.models import *
from django.contrib import messages
from django.contrib.messages import constants


@login_required(login_url='/auth/login/')
def auth_doctor(request):

    if is_medico(request.user):
        messages.add_message(request, constants.ERROR, 'Você já está cadastrado!')
        return redirect(reverse(' '))
    
    else:
        if request.method == "GET":
            areas = MedicineArea.objects.all()
            
            context = {
                'areas': areas,
            }
            return render(request, 'medicine/auth_doctor.html', context=context)
        
        else:
            crm = request.POST['crm']
            nome_completo = request.POST['nome']
            cep = request.POST['cep']
            rua = request.POST['rua']
            bairro = request.POST['bairro']
            numero = request.POST['numero']
            rg = request.FILES['rg']
            foto_perfil = request.FILES['foto']
            cedula_identidade_medica = request.FILES['cim']
            descricao = request.POST['descricao']  
            valor_consulta = request.POST['valor_consulta']
            area = request.POST['especialidade']

            # TODO: validar campos

            medico = MedicoData.objects.create(
                crm=crm,
                nome_completo=nome_completo,
                cep=cep,
                rua=rua,
                bairro=bairro,
                numero=numero,
                rg=rg,
                foto_perfil=foto_perfil,
                cedula_identidade_medica=cedula_identidade_medica,
                descricao=descricao,
                valor_consulta=valor_consulta,
                user=request.user,
                area_id=area,
            )

            medico.save()
            
            messages.add_messages(request, constants.SUCESS, 'Médico cadastrado!')
            return redirect(reverse('auth_doctor'))
