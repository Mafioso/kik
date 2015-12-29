$( document ).ready(function(){
	function return_guarant_json(row){
		data = {
	    		"personal_data": {
	    			 "last_name": $($(row).find('input')[0]).val(),
	    			 "first_name": $($(row).find('input')[1]).val(),
	    			 "middle_name": $($(row).find('input')[2]).val(),
	    			 "date_of_birth": $($(row).find('input')[3]).val(),
	    			 "birth_place": $($(row).find('input')[4]).val(),
	    			 "sex": $($(row).find('input')[5]).val(),
	    			 "education": $($(row).find('input')[6]).val(),
	    			 "iin": $($(row).find('input')[7]).val(),
	    			 "id_number": $($(row).find('input')[8]).val(),
	    			 "given_by": $($(row).find('input')[9]).val(),
	    			 "date_of_receive": $($(row).find('input')[10]).val(),
	    			 "valid_till": $($(row).find('input')[11]).val()
	    		},
	    		"form":{
	    			"family_data":{
	    				 "name": $($(row).find('input')[12]).val(),
	    				 "kids_num": $($(row).find('input')[13]).val(),
	    				 "dependant": $($(row).find('input')[14]).val()
	    				},
	    			"address_data":{
	    				"registered":{
	    					"postal_code": $($(row).find('input')[15]).val(),
	    					"state": $($(row).find('input')[16]).val(),
	    					"district": $($(row).find('input')[17]).val(),
	    					"town_name": $($(row).find('input')[18]).val(),
	    					"street": $($(row).find('input')[19]).val(),
	    					"house_no": $($(row).find('input')[20]).val(),
	    					"apartment_no": $($(row).find('input')[21]).val(),
	    					"phone_no": $($(row).find('input')[22]).val(),
	    					"date_registered": $($(row).find('input')[23]).val()
	    					},
	    				"actual":{
	    					"postal_code": $($(row).find('input')[24]).val(),
	    					"state": $($(row).find('input')[25]).val(),
	    					"district": $($(row).find('input')[26]).val(),
	    					"town_name": $($(row).find('input')[27]).val(),
	    					"street": $($(row).find('input')[28]).val(),
	    					"house_no": $($(row).find('input')[29]).val(),
	    					"apartment_no": $($(row).find('input')[30]).val(),
	    					"phone_no": $($(row).find('input')[31]).val(),
	    					"date_registered": $($(row).find('input')[32]).val()
	    					}
	    				},
	    			"job_data":{
	    				"main_job_data":{
	    					"org_name": $($(row).find('input')[33]).val(),
	    					"address": $($(row).find('input')[34]).val(),
	    					"position": $($(row).find('input')[35]).val(),
	    					"organization_work_years_num": $($(row).find('input')[36]).val(),
	    					"work_years_num": $($(row).find('input')[37]).val(),
	    					"phone_fax": $($(row).find('input')[38]).val()
	    					},
	    				"additional_job_data":[
	    						{
	    							"organization_name": $($(row).find('input')[39]).val(),
	    							"position": $($(row).find('input')[40]).val()
	    						}
	    					]
	    				},
	    			"income_data":{
	    				 "main_job": $($(row).find('input')[41]).val(),
	    				 "additional_job": $($(row).find('input')[42]).val(),
	    				 "devidents": $($(row).find('input')[43]).val(),
	    				 "insurance": $($(row).find('input')[44]).val(),
	    				 "pension": $($(row).find('input')[45]).val(),
	    				 "lease": $($(row).find('input')[46]).val(),
	    				 "alimony": $($(row).find('input')[47]).val(),
	    				 "other": $($(row).find('input')[48]).val(),
	    				 "total": $($(row).find('input')[49]).val()
	    				},
	    			"expenses_data":{
	    				 "everyday": $($(row).find('input')[50]).val(),
	    				 "alimony": $($(row).find('input')[51]).val(), 
	    				 "taxes": $($(row).find('input')[52]).val(),
	    				 "insurance_estate": $($(row).find('input')[53]).val(),
	    				 "insurance_life": $($(row).find('input')[54]).val(),
	    				 "bank_loan": $($(row).find('input')[55]).val(),
	    				 "utilities": $($(row).find('input')[56]).val(),
	    				 "rent": "",
	    				 "other": $($(row).find('input')[57]).val(),
	    				 "total": $($(row).find('input')[58]).val()
	    				},
	    			"contact_data":{
	    				"home_phone_no": $($(row).find('input')[59]).val(),
	    				"mobile_phone_1_no": $($(row).find('input')[60]).val(),
	    				"mobile_phone_2_no": $($(row).find('input')[61]).val(),
	    				"email": $($(row).find('input')[62]).val() 
	    				}
	    		}
		}
		return data
	}

    $('.btn_type_t_1159b86').click(function(){
    	var guarant_rows = $('.trow')
    	var guarant_array = []
    	for (var i=0; i<guarant_rows.length; i++){
    		guarant_array.push(return_guarant_json($(guarant_rows[i])))
    	}
    	if ($("#f_81704d2_true").attr('checked')=='checked'){
	        var stage = 'initial';
	    }
	    else{
	    	var stage = 'secondary';
	    }
	    var gcvp = $('#conditions_table').find('a')[0];
	    console.log(gsvp);
        json = {
            "document_id" : $('#msf_id').val().split(':')[2],
            "gcvp":$(gcvp).attr('href'),
            "guarants": guarant_array,
            "stage":stage,
        	"conditions_data":{
        		 "room_num": $('#').val(),
        		 "area": $('#js_f_8135d97').val(),
        		 "price": $('#js_f_b1b67b2').val(),
        		 "program": $('#').val(),
        		 "rent_duration": $('#js_f_117edfc').val(),
        		 "price_per_meter": $('#js_f_e170f7c').val(),
        		 "rent_amount": $('#').val()
        		},
        	"renter": {
        		"personal_data": {
        			 "date_of_receive": $('#js_f_0133645').val(),
        			 "date_of_birth": $('#js_f_119eb57').val(),
        			 "iin": $('#js_f_61ec152').val(),
        			 "first_name": $('#js_f_a1147ce').val(),
        			 "given_by": $('#js_f_31a0632').val(),
        			 "birth_place": $('#js_f_51f46cd').val(),
        			 "education": $('#js_f_a174c3e').val(),
        			 "middle_name": $('#js_f_b1f43f7').val(),
        			 "sex": $('#').val(),
        			 "valid_till": $('#js_f_412fec3').val(),
        			 "last_name": $('#js_f_f1231f9').val(),
        			 "id_number": $('#js_f_71823fd').val()
        			},
        		"form":{
        			"family_data":{
        				 "name":$('#js_f_81cd184').val(),
        				 "kids_num":$('#js_f_01fb637').val(),
        				 "dependant":$('#js_f_c1ea907').val()
        				},
        			"address_data":{
        				"registered":{
        					"town_name": $('#js_f_411ebab').val(),
        					"date_registered": $('#js_f_41ce7ed').val(),
        					"house_no": $('#js_f_c1ad224').val(),
        					"postal_code": $('#js_f_0126779').val(),
        					"apartment_no": $('#js_f_e1c1dae').val(),
        					"street": $('#js_f_d18ed11').val(),
        					"state": $('#js_f_61aa838').val(),
        					"district": $('#js_f_a137d40').val(),
        					"phone_no": $('#js_f_a17fd08').val()
        					},
        				"actual":{
        					"town_name": $('#js_f_a11ebd6').val(),
        					"date_registered": $('#js_f_a1d53ff').val(),
        					"house_no": $('#js_f_8105681').val(),
        					"postal_code": $('#js_f_e189776').val(),
        					"apartment_no": $('#js_f_01ccd27').val(),
        					"street": $('#js_f_a1399a6').val(),
        					"state": $('#js_f_71ac0a8').val(),
        					"district": $('#js_f_6175d3d').val(),
        					"phone_no": $('#js_f_01d9d29').val()
        					}
        				},
        			"contact_data":{
        				"home_phone_no": $('#js_f_c1dabdd').val(),
        				"mobile_phone_1_no": $('#js_f_e1d43b5').val(),
        				"mobile_phone_2_no": $('#js_f_41fedac').val(),
        				"email": $('#js_f_21866d3').val()
        				},
        			"job_data":{
        				"main_job_data":{
        					"org_name": $('#js_f_7189eab').val(),
        					"address": $('#js_f_514888c').val(),
        					"position": $('#js_f_916bc22').val(),
        					"organization_work_years_num": $('#js_f_1197237').val(),
        					"work_years_num": $('#js_f_c119e19').val(),
        					"phone_fax": $('#js_f_01a3425').val()
        					},
        				"additional_job_data":[
        						{
        							"organization_name": $('#js_f_815d906').val(),
        							"position": $('#js_f_d18c9d9').val()
        						}
        					]
        				},
        			"income_data":{
        				 "lease": $('#js_f_7140a96').val(),
        				 "insurance": $('#js_f_214e7a7').val(),
        				 "devidents": $('#js_f_51a3765').val(),
        				 "other": $('#js_f_11c0511').val(),
        				 "total": $('#js_f_81da5e7').val(),
        				 "pension": $('#js_f_c157761').val(),
        				 "alimony": $('#js_f_814247f').val(),
        				 "additional_job": $('#js_f_d14e3d8').val(),
        				 "main_job": $('#js_f_b13371b').val()
        				},
        			"expenses_data":{
        				 "bank_loan": $('#js_f_41642ac').val(),
        				 "rent": $('#js_f_d1e8dd6').val(),
        				 "total": $('#js_f_d1e35f9').val(),
        				 "utilities": $('#js_f_e1c7666').val(),
        				 "insurance_life": $('#js_f_019b413').val(),
        				 "insurance_estate": $('#js_f_716b1e8').val(),
        				 "everyday": $('#js_f_31b2267').val(),
        				 "other": $('#js_f_115bfb1').val(),
        				 "taxes": $('#js_f_0199dba').val(),
        				 "alimony": $('#js_f_413dabb').val()
        				}
        		}
        	},
        	"msap": $('#js_f_511ef9a').val(),
        	"lpk":{
        		"p_d": $("#js_f_c1489c7").val(),
        		"o_d": $("#js_f_419cb00").val()
        	}
        };
        console.log(json);
        
        $.ajax({
          type: "POST",
          url: "http://178.88.64.83:8000/api/request/receive/",
          data: "data="+JSON.stringify(json),
          success: function(data){
              console.log(data);
          },
          dataType: 'jsonp'
        });
        
        return false;
    });
    console.log($('#content :input').serializeArray());
    
});