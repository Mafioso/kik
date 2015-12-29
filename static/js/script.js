var $income_elements = $("#edit_field_f_b13371b, "+
  "#edit_field_f_d14e3d8, "+
  "#edit_field_f_51a3765, "+
  "#edit_field_f_214e7a7, "+
  "#edit_field_f_c157761, "+
  "#edit_field_f_7140a96, "+
  "#edit_field_f_814247f, "+
  "#edit_field_f_11c0511");

$income_elements.keyup(function(){
    var sum = 0;
    for (i=0; i < $income_elements.length; i++){
        if (!isNaN(parseFloat($($income_elements[i]).val().replace(/\s/g, '')))){
            sum += parseFloat($($income_elements[i]).val().replace(/\s/g, ''));
        }
    }              
    $("#edit_field_f_81da5e7").val(sum);
    calc_msap();
})

var $expenses_elements = $(
    "#edit_field_f_31b2267, "+
    "#edit_field_f_413dabb, "+
    "#edit_field_f_0199dba, "+
    "#edit_field_f_716b1e8, "+
    "#edit_field_f_019b413, "+
    "#edit_field_f_41642ac, "+
    "#edit_field_f_e1c7666, "+
    "#edit_field_f_d1e8dd6, "+
    "#edit_field_f_115bfb1" 
 );

$expenses_elements.keyup(function(){
    var sum = 0
    for (i=0; i < $expenses_elements.length; i++){
        if (!isNaN(parseFloat($($expenses_elements[i]).val().replace(/\s/g, '')))){
            sum += parseFloat($($expenses_elements[i]).val().replace(/\s/g, ''));
        }
    }           
    $("#edit_field_f_d1e35f9").val(sum);
    calc_msap();
});



var $atomic_inputs = $("#edit_field_f_81da5e7, "+
        "#edit_field_f_d1e35f9, "+
        "#edit_field_f_81da5e7, " +
        "#edit_field_f_d1e35f9, " +
        "#edit_field_f_01f8296, " +
        "#edit_field_f_c1489c7, " +
        "#edit_field_f_419cb00, " +
        "#edit_field_f_b1b67b2, " +
        "#edit_field_f_511ef9a"
    );

$atomic_inputs.keydown(function(e){
    e.preventDefault();
    return false;
})

var $estate_elements = $("#edit_field_f_8135d97, #edit_field_f_e170f7c");

$estate_elements.keyup(function(){
    if ($($estate_elements[0]).val() && $($estate_elements[1]).val()){
        var price = parseFloat($($estate_elements[0]).val().replace(/\s/g, ''))
        var area = parseFloat($($estate_elements[1]).val().replace(/\s/g, ''))
        if (!isNaN(area) && !isNaN(price)){
            $("#edit_field_f_b1b67b2").val(area*price)
            $("#edit_field_f_01f8296").val(area*price)
        }
    }
    calc_msap();
})

var $garant_income = $("input[title='Размер ежемесячной заработной платы по основному месту работы'], " +
    "input[title='Размер ежемесячной заработной платы по дополнительному месту работы'], " +
    "input[title='Доходы в виде дивидендов'], " +
    "input[title='Доходы в виде вознагражд. и регулярных страховых выплат'], " +
    "input[title='Пенсионные выплаты и стипендии'], " +
    "input[title='Доход в виде арендной платы'], " +
    "input[title='Получаемые алименты'], "+
    "input[title='Другие доходы'], "
    )

var $garant_expenses = $("input[title='Постоянные расходы'], " + 
    "input[title='Расходы по уплате алиментов'], " + 
    "input[title='Расходы по налогам на имущество'], " + 
    "input[title='Платеж по страхованию имущества'], " + 
    "input[title='Платеж по страхованию жизни'], " + 
    "input[title='Ежемесячные выплаты по кредитам в банках'], " +
    "input[title='Коммунальные платежи'], " +
    "input[title='Прочие расходы']"
    )

var $guarants_cumulitive_income = 0;
var $guarants_cumulitive_expense = 0;

$garant_income.keyup(function(){
    calc_garant_income()
    calc_msap();
})

$garant_expenses.keyup(function(){
    calc_garant_expenses()
    calc_msap();
});

function calc_garant_income(){
    var sum = 0
    var garant_num = $("input[title='Размер ежемесячной заработной платы по основному месту работы']").length;
    for (var i=0; i<garant_num; i++){
        var paycheck = $("input[title='Размер ежемесячной заработной платы по основному месту работы']")[i]
        if (!isNaN(parseFloat($(paycheck).val().replace(/\s/g, '')))){
            sum += parseFloat($(paycheck).val().replace(/\s/g, ''));
        }
        var additional_paycheck = $("input[title='Размер ежемесячной заработной платы по дополнительному месту работы']")[i]
        if (!isNaN(parseFloat($(additional_paycheck).val().replace(/\s/g, '')))){
            sum += parseFloat($(additional_paycheck).val().replace(/\s/g, ''));
        }
        var devidents = $("input[title='Доходы в виде дивидендов']")[i]
        if (!isNaN(parseFloat($(devidents).val().replace(/\s/g, '')))){
            sum += parseFloat($(devidents).val().replace(/\s/g, ''));
        }
        var insurance = $("input[title='Доходы в виде вознагражд. и регулярных страховых выплат']")[i]
        if (!isNaN(parseFloat($(insurance).val().replace(/\s/g, '')))){
            sum += parseFloat($(insurance).val().replace(/\s/g, ''));
        }
        var insurance_life = $("input[title='Платеж по страхованию жизни']")[i]
        if (!isNaN(parseFloat($(insurance_life).val().replace(/\s/g, '')))){
            sum += parseFloat($(insurance_life).val().replace(/\s/g, ''));
        }
        var pension = $("input[title='Пенсионные выплаты и стипендии']")[i]
        if (!isNaN(parseFloat($(pension).val().replace(/\s/g, '')))){
            sum += parseFloat($(pension).val().replace(/\s/g, ''));
        }
        var rent = $("input[title='Доход в виде арендной платы']" )[i]
        if (!isNaN(parseFloat($(rent).val().replace(/\s/g, '')))){
            sum += parseFloat($(rent).val().replace(/\s/g, ''));
        }
        var alimony = $("input[title='Получаемые алименты']")[i]
        if (!isNaN(parseFloat($(alimony).val().replace(/\s/g, '')))){
            sum += parseFloat($(alimony).val().replace(/\s/g, ''));
        }
        var other = $("input[title='Другие доходы']")[i]
        if (!isNaN(parseFloat($(other).val().replace(/\s/g, '')))){
            sum += parseFloat($(other).val().replace(/\s/g, ''));
        }
        var result = $("input[title='Итого доходов']")[i]
        $(result).val(sum);
        sum=0;
    }
    for (var i=0; i<garant_num; i++){
        if (!isNaN(parseFloat($($("input[title='Итого доходов']")[i]).val().replace(/\s/g, '')))){
            $guarants_cumulitive_income += parseFloat($($("input[title='Итого доходов']")[i]).val().replace(/\s/g, ''));
        }
    }
    calc_msap();
}

function calc_garant_expenses(){
    var sum = 0
    var garant_num = $("input[title='Постоянные расходы']").length;
    for (var i=0; i<garant_num; i++){
        var input = $("input[title='Постоянные расходы']" )[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var input = $("input[title='Расходы по уплате алиментов']" )[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var input = $("input[title='Расходы по налогам на имущество']" )[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var input = $("input[title='Платеж по страхованию имущества']" )[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var input = $("input[title='Платеж по страхованию жизни']" )[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var input = $("input[title='Ежемесячные выплаты по кредитам в банках']")[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var input = $("input[title='Коммунальные платежи']")[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var input = $("input[title='Прочие расходы']")[i];
        if (!isNaN(parseFloat($(input).val().replace(/\s/g, '')))){
            sum += parseFloat($(input).val().replace(/\s/g, ''));
        }
        var result = $("input[title='Итого расходов']")[i]
        $(result).val(sum);
        sum=0;
    }
    for (var i=0; i<garant_num; i++){
        if (!isNaN(parseFloat($($("input[title='Итого расходов']")[i]).val().replace(/\s/g, '')))){
            $guarants_cumulitive_expense += parseFloat($($("input[title='Итого расходов']")[i]).val().replace(/\s/g, ''));
        }
    }
    calc_msap();
}

function calc_garant(){
    var $garant_income = $("input[title='Размер ежемесячной заработной платы по основному месту работы'], " +
        "input[title='Размер ежемесячной заработной платы по дополнительному месту работы'], " +
        "input[title='Доходы в виде дивидендов'], " +
        "input[title='Доходы в виде вознагражд. и регулярных страховых выплат'], " +
        "input[title='Пенсионные выплаты и стипендии'], " +
        "input[title='Доход в виде арендной платы'], " +
        "input[title='Получаемые алименты'], "+
        "input[title='Другие доходы'], "
        )

    var $garant_expenses = $("input[title='Постоянные расходы'], " + 
        "input[title='Расходы по уплате алиментов'], " + 
        "input[title='Расходы по налогам на имущество'], " + 
        "input[title='Платеж по страхованию имущества'], " + 
        "input[title='Платеж по страхованию жизни'], " + 
        "input[title='Ежемесячные выплаты по кредитам в банках'], " +
        "input[title='Коммунальные платежи'], " +
        "input[title='Прочие расходы']"
        )
    calc_garant_income();
    calc_garant_expenses();
    $garant_income.keyup(function(){
        calc_garant_income()
    })
    $garant_expenses.keyup(function(){
        calc_garant_expenses()
    });
    calc_msap();
}

var $cumulative_income = $("#edit_field_f_81da5e7")
var $cumulative_expenses = $("#edit_field_f_d1e35f9")

function calc_msap(){
    var monthly_payment = $("#edit_field_f_01f8296").val().replace(/\s/g, '')
    if (isNaN(monthly_payment)){
        monthly_payment = 0;
    }
    var income1 = parseFloat($($cumulative_income[0]).val().replace(/\s/g, ''))
    if (isNaN(income1)){
        income1 = 0;
    }
    var income2 = $guarants_cumulitive_income
    var pd_result = (monthly_payment/(income1+income2))*100
    $("#edit_field_f_c1489c7").val(pd_result)

    var cum_expenses = $("#edit_field_f_01f8296").val().replace(/\s/g, '')
    if (isNaN(cum_expenses)){
        cum_expenses = 0;
    }
    var expense1 = parseFloat($($cumulative_expenses[0]).val().replace(/\s/g, ''))
    if (isNaN(expense1)){
        expense1 = 0;
    }
    var expense2 = $guarants_cumulitive_expense
    var od_result = (cum_expenses/(income1+income2))*100
    $("#edit_field_f_419cb00").val(od_result)
    
    var all_income = $("#edit_field_f_c1489c7").val()
    var all_expense = $("#edit_field_f_419cb00").val()
    $("#edit_field_f_511ef9a").val(income1 + income2 - expense1 - expense2)
}

$(document).bind("DOMSubtreeModified", calc_garant);
$(document).bind("DOMSubtreeModified", check_request_stage);

function hide_divs(){
    $('#referenceAutocomplete_f_a138e93').parent().parent().parent().parent().hide();
    $('#referenceAutocomplete_f_f19a01c').parent().parent().parent().parent().hide();
    $('#edit_field_f_5163d45').parent().parent().parent().hide();
    $("#edit_field_f_0149ce2").parent().parent().parent().hide();
    $("#edit_field_f_b1141d9").parent().parent().parent().hide();
    $("#edit_field_f_61b7edf").parent().parent().parent().hide();
    $("#edit_field_f_01f8296").parent().parent().hide();

    $("#arend_contact_data").hide();

    $($("tr[class='title']").find('td')[60]).hide()
    $($("tr[class='title']").find('td')[61]).hide()
    $($("tr[class='title']").find('td')[62]).hide()
    $($("tr[class='title']").find('td')[63]).hide()

    var trs = $("tr[class='trow']")
    for (var i=0; i<trs.length; i++){
        $($(trs[i]).find('td')[60]).hide();
        $($(trs[i]).find('td')[61]).hide();
        $($(trs[i]).find('td')[62]).hide();
        $($(trs[i]).find('td')[63]).hide();
    }


}

function show_divs(){
    $('#referenceAutocomplete_f_a138e93').parent().parent().parent().parent().show();
    $('#referenceAutocomplete_f_f19a01c').parent().parent().parent().parent().show();
    $('#edit_field_f_5163d45').parent().parent().parent().show();
    $("#edit_field_f_0149ce2").parent().parent().parent().show();
    $("#edit_field_f_b1141d9").parent().parent().parent().show();
    $("#edit_field_f_61b7edf").parent().parent().parent().show();
    $("#edit_field_f_01f8296").parent().parent().show();

    $("#arend_contact_data").show();

    $($("tr[class='title']").find('td')[60]).show()
    $($("tr[class='title']").find('td')[61]).show()
    $($("tr[class='title']").find('td')[62]).show()
    $($("tr[class='title']").find('td')[63]).show()

    var trs = $("tr[class='trow']")
    for (var i=0; i<trs.length; i++){
        $($(trs[i]).find('td')[60]).show();
        $($(trs[i]).find('td')[61]).show();
        $($(trs[i]).find('td')[62]).show();
        $($(trs[i]).find('td')[63]).show();
    }
}

$("#f_81704d2_true").click(function(){
    hide_divs()
})

$("#f_81704d2_false").click(function(){
    show_divs()
})


$("#edit_field_f_117edfc, #edit_field_f_e170f7c, #edit_field_f_8135d97").keyup(function(){
    var lease_duration = parseFloat($("#edit_field_f_117edfc").val().replace(/\s/g, ''))
    if (isNaN(lease_duration)){
        lease_duration = 0;
    }
    var area = parseFloat($("#edit_field_f_e170f7c").val().replace(/\s/g, ''))
    if (isNaN(area)){
        area = 0;
    } 
    var price_per_m = parseFloat($("#edit_field_f_8135d97").val().replace(/\s/g, ''))
    if (isNaN(price_per_m)){
        price_per_m = 0;
    }
    $("#edit_field_f_b1b67b2").val(lease_duration*price_per_m*area)
    calc_msap();
})

$('#searchiin').click(function(){
    $.ajax({type: "POST",
            crossDomain : true,
            url: "http://178.88.64.83:8000/api/request/find/",
            data: 'iin='+$('#search_iin').val(),
            dataType: "jsonp",
    }).done(function(json){
        Object.byString = function(o, s) {
            s = s.replace(/\[(\w+)\]/g, '.$1'); // convert indexes to properties
            s = s.replace(/^\./, '');           // strip a leading dot
            var a = s.split('.');
            for (var i = 0, n = a.length; i < n; ++i) {
                var k = a[i];
                if (k in o) {
                    o = o[k];
                } else {
                    return '';
                }
            }
            return o;
        }
        
        $('#').val(Object.byString(json, 'conditions_data.room_num'));
        $('#edit_field_f_8135d97').val(Object.byString(json, 'conditions_data.area'));
        $('#edit_field_f_b1b67b2').val(Object.byString(json, 'conditions_data.price'));
        $('#').val(Object.byString(json, 'conditions_data.program'));
        $('#edit_field_f_117edfc').val(Object.byString(json, 'conditions_data.rent_duration'));
        $('#edit_field_f_e170f7c').val(Object.byString(json, 'conditions_data.price_per_meter'));
        $('#').val(Object.byString(json, 'conditions_data.rent_amount'));
        
        $('#edit_field_f_0133645').val(Object.byString(json, 'renter.personal_data.date_of_receive'));
        $('#edit_field_f_119eb57').val(Object.byString(json, 'renter.personal_data.date_of_birth'));
        $('#edit_field_f_61ec152').val(Object.byString(json, 'renter.personal_data.iin'));
        $('#edit_field_f_a1147ce').val(Object.byString(json, 'renter.personal_data.first_name'));
        $('#edit_field_f_31a0632').val(Object.byString(json, 'renter.personal_data.given_by'));
        $('#edit_field_f_51f46cd').val(Object.byString(json, 'renter.personal_data.birth_place'));
        $('#edit_field_f_a174c3e').val(Object.byString(json, 'renter.personal_data.education'));
        $('#edit_field_f_b1f43f7').val(Object.byString(json, 'renter.personal_data.middle_name'));
        $('#').val(Object.byString(json, 'renter.personal_data.sex'));
        $('#edit_field_f_412fec3').val(Object.byString(json, 'renter.personal_data.valid_till'));
        $('#edit_field_f_f1231f9').val(Object.byString(json, 'renter.personal_data.last_name'));
        $('#edit_field_f_71823fd').val(Object.byString(json, 'renter.personal_data.id_number'));
        
        $('#edit_field_f_81cd184').val(Object.byString(json, 'renter.form.family_data.name'));
        $('#edit_field_f_01fb637').val(Object.byString(json, 'renter.form.family_data.kids_num'));
        $('#edit_field_f_c1ea907').val(Object.byString(json, 'renter.form.family_data.dependant'));
        
        $('#edit_field_f_411ebab').val(Object.byString(json, 'renter.form.address_data.registered.town_name'));
        $('#edit_field_f_41ce7ed').val(Object.byString(json, 'renter.form.address_data.registered.date_registered'));
        $('#edit_field_f_c1ad224').val(Object.byString(json, 'renter.form.address_data.registered.house_no'));
        $('#edit_field_f_0126779').val(Object.byString(json, 'renter.form.address_data.registered.postal_code'));
        $('#edit_field_f_e1c1dae').val(Object.byString(json, 'renter.form.address_data.registered.apartment_no'));
        $('#edit_field_f_d18ed11').val(Object.byString(json, 'renter.form.address_data.registered.street'));
        $('#edit_field_f_61aa838').val(Object.byString(json, 'renter.form.address_data.registered.state'));
        $('#edit_field_f_a137d40').val(Object.byString(json, 'renter.form.address_data.registered.district'));
        $('#edit_field_f_a17fd08').val(Object.byString(json, 'renter.form.address_data.registered.phone_no'));
        
        $('#edit_field_f_a11ebd6').val(Object.byString(json, 'renter.form.address_data.actual.town_name'));
        $('#edit_field_f_a1d53ff').val(Object.byString(json, 'renter.form.address_data.actual.date_registered'));
        $('#edit_field_f_8105681').val(Object.byString(json, 'renter.form.address_data.actual.house_no'));
        $('#edit_field_f_e189776').val(Object.byString(json, 'renter.form.address_data.actual.postal_code'));
        $('#edit_field_f_01ccd27').val(Object.byString(json, 'renter.form.address_data.actual.apartment_no'));
        $('#edit_field_f_a1399a6').val(Object.byString(json, 'renter.form.address_data.actual.street'));
        $('#edit_field_f_71ac0a8').val(Object.byString(json, 'renter.form.address_data.actual.state'));
        $('#edit_field_f_6175d3d').val(Object.byString(json, 'renter.form.address_data.actual.district'));
        $('#edit_field_f_01d9d29').val(Object.byString(json, 'renter.form.address_data.actual.phone_no'));
        
        $('#edit_field_f_c1dabdd').val(Object.byString(json, 'renter.form.contact_data.home_phone_no'));
        $('#edit_field_f_e1d43b5').val(Object.byString(json, 'renter.form.contact_data.mobile_phone_1_no'));
        $('#edit_field_f_41fedac').val(Object.byString(json, 'renter.form.contact_data.mobile_phone_2_no'));
        $('#edit_field_f_21866d3').val(Object.byString(json, 'renter.form.contact_data.email'));
        
        $('#edit_field_f_7189eab').val(Object.byString(json, 'renter.form.job_data.main_job_data.org_name'));
        $('#edit_field_f_514888c').val(Object.byString(json, 'renter.form.job_data.main_job_data.address'));
        $('#edit_field_f_916bc22').val(Object.byString(json, 'renter.form.job_data.main_job_data.position'));
        $('#edit_field_f_1197237').val(Object.byString(json, 'renter.form.job_data.main_job_data.organization_work_years_num'));
        $('#edit_field_f_c119e19').val(Object.byString(json, 'renter.form.job_data.main_job_data.work_years_num'));
        $('#edit_field_f_01a3425').val(Object.byString(json, 'renter.form.job_data.main_job_data.phone_fax'));
        
        $('#edit_field_f_815d906').val(Object.byString(json, 'renter.form.job_data.additional_job_data.0.organization_name'));
        $('#edit_field_f_d18c9d9').val(Object.byString(json, 'renter.form.job_data.additional_job_data.0.position'));
        
        $('#edit_field_f_7140a96').val(Object.byString(json, 'renter.form.income_data.lease'));
        $('#edit_field_f_214e7a7').val(Object.byString(json, 'renter.form.income_data.insurance'));
        $('#edit_field_f_51a3765').val(Object.byString(json, 'renter.form.income_data.devidents'));
        $('#edit_field_f_11c0511').val(Object.byString(json, 'renter.form.income_data.other'));
        $('#edit_field_f_81da5e7').val(Object.byString(json, 'renter.form.income_data.total'));
        $('#edit_field_f_c157761').val(Object.byString(json, 'renter.form.income_data.pension'));
        $('#edit_field_f_814247f').val(Object.byString(json, 'renter.form.income_data.alimony'));
        $('#edit_field_f_d14e3d8').val(Object.byString(json, 'renter.form.income_data.additional_job'));
        $('#edit_field_f_b13371b').val(Object.byString(json, 'renter.form.income_data.main_job'));
        
        $('#edit_field_f_41642ac').val(Object.byString(json, 'renter.form.expenses_data.bank_loan'));
        $('#edit_field_f_d1e8dd6').val(Object.byString(json, 'renter.form.expenses_data.rent'));
        $('#edit_field_f_d1e35f9').val(Object.byString(json, 'renter.form.expenses_data.total'));
        $('#edit_field_f_e1c7666').val(Object.byString(json, 'renter.form.expenses_data.utilities'));
        $('#edit_field_f_019b413').val(Object.byString(json, 'renter.form.expenses_data.insurance_life'));
        $('#edit_field_f_716b1e8').val(Object.byString(json, 'renter.form.expenses_data.insurance_estate'));
        $('#edit_field_f_31b2267').val(Object.byString(json, 'renter.form.expenses_data.everyday'));
        $('#edit_field_f_115bfb1').val(Object.byString(json, 'renter.form.expenses_data.other'));
        $('#edit_field_f_0199dba').val(Object.byString(json, 'renter.form.expenses_data.taxes'));
        $('#edit_field_f_413dabb').val(Object.byString(json, 'renter.form.expenses_data.alimony'));
    });
    return false;
});

function check_request_stage(){
    if ($("#f_81704d2_true").attr('checked')=='checked'){
        hide_divs();
    }
}

$(document).ready(function(){
    check_request_stage()
})